from jinja2 import Environment, FileSystemLoader
import re
import logging
import os
import artsemLib
from collections import namedtuple

__install_dir__ = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
# __db__ = TinyDB(os.path.join(__install_dir__, 'conf', 'db.json'))  # TODO: create cache-db

# LOAD ARTSEM CONFIG
try:
    import yaml

    with open(os.path.join(__install_dir__, 'conf', 'conf.yml'), 'r') as conffile:
        _conf = yaml.safe_load(conffile)
        logging.info(f"Configuration loaded: {_conf}")
except Exception:
    logging.exception(f"Unexpected error loading configuration (artsem/conf/conf.yml)")
    exit(100)


def _parse_args():
    """Parses input arguments

    TODO: sub-parsers
    artsem list (sub parser) search all, by name, id...
        [modules | errors | templates]
        -q <query>
    artsem create (sub parser) TODO: future
        modules NAME
        error ID LABEL DESC
        template
    artsem (normal cli)
        TARGETS
        (-e, --exclude) ^ (-i, --include)
        # Mutually exclusive group -o or --template
        -O, --output -> Name for output file. File format is deduced from templates name.
                        As many output files as outputs specified
                        out.html -> html format, out.md -> md format, out -> txt format, out.json -> json format, ...
        --template -> template name or id. By default 'brief.<ext>' of the corresponding formatter.
        Show templates: artsem list templates

    :return: Parsed input arguments
    """
    import argparse
    parser = argparse.ArgumentParser(
        prog=os.path.split(__file__)[1],
        description="Obfuscation analyzer for ELF binaries. "
                    "Select the modules for the analysis and the target files. "
                    "Generate templates formats in different formats",
        epilog="***  Anti-Reversing Trace Scanner for ELF Malware (ARTSEM), by uRHL  ***")
    parser.add_argument(
        "targets",
        nargs='+',
        help="ELF file (single analysis) or ELF Directory (batch analysis)",
        type=str)
    parser.add_argument(
        "-v",
        action="count",
        default=0,
        help="Increase logging verbosity [-v, -vv]")
    parser.add_argument(
        "-O", "--output",
        nargs='+',
        metavar="[TEMPLATE:]OUT_FILE",
        type=str,
        help="Output written into file. As many output files as file names provided in this list. "
             "The format is deduced from the file extension: "
             "out -> txt format, out.html -> html format, out.json -> json format, [...] ."
             "Use `artsem.py list formats` to show all available formatters in this version. "
             "If not provided, the output is only written to the console."
             ""
             "TEMPLATE is optional, and indicates the template to be used. "
             "The template extension and outfile extension must match. "
             "If none, the 1st template (alphabetically) of the parser derived from OUT_FILE is used. Examples: "
             "brief.html:templates, brief:templates.html, T-001:templates, templates.html"
    )
    # TODO: choices =  list(__db__.templates.all().getNames())
    filter_group = parser.add_mutually_exclusive_group()
    filter_group.add_argument(
        "-i", "--include",
        type=int,
        metavar="ProbeID",
        nargs="+",
        help="Only specified Probes (IDs) are executed")
    filter_group.add_argument(
        "-e", "--exclude",
        metavar="ProbeID",
        nargs="+",
        help="Specified Probes (IDs) are excluded, the rest are executed")
    _args = parser.parse_args()
    if _args.v == 0:
        __log_level__ = 'WARN'
    elif _args.v == 1:
        __log_level__ = 'INFO'
    else:
        __log_level__ = 'DEBUG'
    logging.basicConfig(level=__log_level__, force=True)
    logging.debug(f"CLI args: {_args}")
    return _args


def validate_out_writers(writers):
    OutWriter = namedtuple('OutWriter', ['template', 'outfile'])
    logging.info("Validating output writers")
    _ret = list()
    if writers is None:
        logging.debug(f"Default Output Writer will be selected")
        _ret.append(OutWriter(_conf.get('default_template'),
                              f"{_conf.get('default_report_name')}"
                              f"{os.path.splitext(_conf.get('default_template'))[1]}"))
    elif isinstance(writers, list):
        for i in args.output:
            if re.fullmatch('([\\w\\.-]+:)?[\\w\\.-]*', i, flags=re.I) is None:
                raise SyntaxError(f"Invalid argument syntax. Expected [TEMPALTE:]OUTFILE, obtained '{i}'")
            else:
                _ret.append(
                    OutWriter(*i.split(':')) if i.find(':') != -1 else OutWriter(_conf.get('default_template'), i))
    else:
        raise TypeError(f"Expected list, obtained '{type(writers)}'")

    logging.info(f"({len(_ret)}) Output writers validated")
    logging.debug(f"Output writers: {_ret}")
    return _ret


def flat_target_list(path_list):
    # Combine all input sources in a single list, with at least 1 elem
    logging.info("Validating input files")
    _ret = list()
    _fails = 0
    _total = 0
    for tg in list(set([os.path.abspath(tgfile) for tgfile in path_list])):
        _total += 1
        if os.path.isdir(tg):
            _ret.extend([os.path.abspath(f) for f in os.listdir(tg)])
        elif os.path.isfile(tg):
            _ret.append(tg)
        else:
            logging.warning(f"Invalid target ({tg})")
            _fails += 1
    logging.info(f"({_total}) Input files validated. Successful: {len(_ret)}. Failed: {_fails}")
    return _ret


if __name__ == '__main__':
    args = _parse_args()
    logging.debug(f"Installation dir found: {__install_dir__}")

    _analysis = artsemLib.AnalysisMatrix()
    _analysis.full_load(
        probes=os.path.join(__install_dir__, 'artsem', 'main', 'modules'),
        subj_list=flat_target_list(args.targets))
    _analysis.analyze(include=args.include, exclude=args.exclude)

    logging.info("Final step. Generating reports")
    logging.info("Loading templates")
    environment = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))
    logging.info(f"({len(environment.list_templates())}) templates loaded")
    for writer in validate_out_writers(args.output):
        logging.info("Generating reports")
        try:
            template = environment.get_template(writer.template)
            logging.debug(f"Using template '{writer.template}'")
            with open(writer.outfile, mode="w", encoding="utf-8") as report:
                report.write(template.render(analysis=_analysis))
            logging.info(f"Report '{writer.outfile}' generated successfully")
        except Exception:
            logging.exception(f"Error generating report '{writer.outfile}'")
    logging.info("Program execution successful. Exiting...")
    exit(200)
