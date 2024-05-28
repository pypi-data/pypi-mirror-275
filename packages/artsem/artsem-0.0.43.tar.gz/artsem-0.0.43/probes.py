import logging as _log
from collections import namedtuple as _nt
from subprocess import call as _subprocess_call
from os import path as _os_path, walk as _os_walk
from yaml import safe_load as _yaml_safe_load
from pandas import DataFrame as _DataFrame, Series as _Series
from checksumdir import dirhash


def filehash(fpath):
    from hashlib import md5, sha1, sha256
    try:
        with open(fpath, 'rb') as _file:
            _fcontent = _file.read()
            return {
                'md5': md5(_fcontent).hexdigest(),
                'sha1': sha1(_fcontent).hexdigest(),
                'sha256': sha256(_fcontent).hexdigest()
            }
    except FileNotFoundError:
        _log.warning(f"The target file is not found ({fpath})")
        return {'md5': '', 'sha1': '', 'sha256': ''}


class Subject:

    def __init__(self, fpath):
        if not Subject.validate_path(fpath):
            raise ValueError(f"Not an ELF {fpath}")
        self.path = fpath
        self.hash = filehash(fpath)

    @staticmethod
    def validate_path(fpath):
        # TODO: assert is elf file
        return _os_path.isfile(fpath)

    @property
    def filename(self):
        return _os_path.basename(self.path)

    def __repr__(self):
        return self.filename

    def to_json(self):
        # Exclude self.hash. Computed when the instance is initialized
        return {'path': self.path, 'hash': self.hash}


class Probe:
    _ReturnCode = _nt('ReturnCode', ['label', 'value'])

    __return_codes__ = {
        _ReturnCode('positive', 0),
        _ReturnCode('negative', 1),
        _ReturnCode('fail', 2),
        _ReturnCode('undetermined', 3),
        _ReturnCode('undefined', 4)
    }

    def __init__(self, dirpath):
        if not Probe.validate_probe_structure(dirpath):
            raise ValueError("Not parser directory. Missing 'main.py' and/or conf.yml file")
        self.root_dir = dirpath
        with open(_os_path.join(dirpath, 'conf.yml'), 'r') as pbconffile:
            self.conf = _yaml_safe_load(pbconffile)
            self.conf.update({'sha256': dirhash(_os_path.dirname(dirpath), "sha256")})

    @property
    def name(self):
        return _os_path.basename(self.root_dir)

    @property
    def exec_path(self):
        return _os_path.abspath(_os_path.join(self.root_dir, 'main.py'))

    def __repr__(self):
        return f"{self.name} ({self.conf.get('id')})"

    @staticmethod
    def validate_probe_structure(dirpath) -> bool:
        """

        :param dirpath: Dir path pointing to a modules dir
        :return: True if dirpath points to a valid modules dir. False otherwise
        """
        return _os_path.isfile(_os_path.join(dirpath, 'main.py')) and _os_path.isfile(_os_path.join(dirpath, 'conf.yml'))

    def run(self, target_path) -> _ReturnCode:
        """Execute this modules on a target
        Prepares the environment to execute the modules, then runs it, and finally validates the result

        Result validation
            Checks if res in within allowed return codes.
            If it's found, returns the associated `ReturnCode` instance
            If it's not found, 'undetermined' ReturnCode will be returned

        :param target_path: path to the file to be analyzed
        :return: an integer number. Check the docs for more info about return codes
        """

        _log.info(f"Executing modules '{self.name}' on target '{target_path}'")
        ret = _subprocess_call(f"{self.exec_path} {target_path}", shell=True)
        if ret not in [rc.value for rc in Probe.__return_codes__]:
            _validated_res = list(filter(lambda x: x.label == 'undefined', Probe.__return_codes__))[0]
        else:
            _validated_res = list(filter(lambda x: x.value == ret, Probe.__return_codes__))[0]
        _log.info(f"Probe '{self.name}' {_validated_res.label} ({ret})")
        return _validated_res

    def parse_cli(self, cmd=None):
        import argparse
        parser = argparse.ArgumentParser(
            prog=_os_path.join(self.name, 'main.py'),
            description=self.conf.get('description')
        )
        parser.add_argument('target', help="Path to target (ELF) file to be analyzed")
        _args = parser.parse_args(cmd)
        _args.__setattr__('probe_conf', self.conf)
        return _args


class AnalysisMatrix:

    def __init__(self):
        self.matrix = _DataFrame(columns=['Probe'])

    def count_probes(self):
        return self.matrix.shape[0]

    def count_targets(self):
        return self.matrix.shape[1] - 1

    def load_subjects(self, subj_list: list):
        if not isinstance(subj_list, list):
            raise TypeError(f"Unexpected type ({type(subj_list)}) for param 'subj_list'. Expected: list")
        for fpath in subj_list:
            try:
                # Add column 'Subject' at the end of the matrix
                self.matrix.insert(
                    self.matrix.shape[1],
                    Subject(fpath),
                    _Series(["Pending"] * self.count_probes()),
                    False)
            except ValueError:
                _log.error(f"Not an ELF {fpath}. Skipping this target")

    def add_probe(self, pb_path):
        if not Probe.validate_probe_structure(pb_path):
            _log.error(f"Not a Probe directory ({pb_path})")
            return
        self.matrix.loc[len(self.matrix)] = [Probe(pb_path)]

    def load_probes(self, prob_list: list):
        if not isinstance(prob_list, list):
            raise TypeError(f"Unexpected type ({type(prob_list)}) for param 'subj_list'. Expected: list")
        # Iterate (absolute path) entries in this directory and filter by the sub-files included in it
        _log.info("Loading probes")
        for i in filter(Probe.validate_probe_structure, prob_list):
            try:
                self.add_probe(i)
            except ValueError:
                continue
        _log.info(f"({self.count_probes()}) Probes loaded: {[x.name for x in self.matrix['Probe']]}")

    def load_probes_from_dir(self, dirpath):
        # https://stackoverflow.com/questions/141291/how-to-list-only-top-level-directories-in-python
        self.load_probes([_os_path.join(dirpath, d) for d in next(_os_walk(dirpath))[1]])

    def full_load(self, probes, subj_list):
        if isinstance(probes, list):
            self.load_probes(probes)
        elif _os_path.isdir(probes):
            self.load_probes_from_dir(probes)
        else:
            raise ValueError(f"Unexpected value for param 'probes'. Expected: list, dir-path")
        self.load_subjects(subj_list)

    def analyze(self, include=None, exclude=None):
        # TODO: run all the corresponding modules
        # TODO: apply parallelism. The computations of each item are independent from the rest
        """
        Analyze the current Matrix
        :param include: If not None, only those Probe IDs within the list will be executed
        :param exclude: If not None, only those Probe IDs NOT IN this list are executed
        :return: None
        """
        _log.info("Starting matrix analysis\n")
        for tg in self.matrix.columns[1:]:
            _log.info(f"Starting subject analysis ({tg.filename})")
            for y_coord, probe in enumerate(self.matrix["Probe"]):
                if (include is not None and probe.id in include) or (exclude is not None and probe.id not in exclude):
                    self.matrix.at[y_coord, tg] = probe.run(tg).label
                elif include is not None or exclude is not None:
                    # If either params is not None and this clause is reached => filter was not passed
                    self.matrix.at[y_coord, tg] = "Excluded"
                else:  # If both are None, probes are not filtered, thus all of them are run
                    self.matrix.at[y_coord, tg] = probe.run(tg).label
            _log.info(f"Subject analysis completed ({tg.filename})\n")
        _log.info(f"Matrix analysis completed. All ({self.count_targets()}) subjects analyzed")

    def load_json(self):
        # TODO: implement
        pass

    def to_json(self):
        # TODO: implement
        pass

    def to_excel(self):
        # TODO: implement
        # 3 pages: results, Probes, Targets,
        pass
