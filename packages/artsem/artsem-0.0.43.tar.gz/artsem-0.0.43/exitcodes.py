import logging
import os.path as _os_path
from tinydb import TinyDB, Query


# Auto-generated file. Modify install_dir/conf/exitcodes.csv instead


def search_exitcode_by_id(exitcode: int) -> list:
    Exitcodes = Query()
    return TinyDB(_os_path.join(*'../../conf/db.json'.split('/'))).table('Exitcodes').search(
        Exitcodes.id == int(exitcode))


def stringify_exitcode(exitcode: int, detail=None):
    detail = f":\n{detail}" if detail is not None else ''
    if isinstance(exitcode, int):
        excode = search_exitcode_by_id(exitcode)
        if excode is None or len(excode) == 0:
            raise ValueError(f"Specified ProbeID ({exitcode}) does not exists")
            # logging.error(f"Specified ProbeID ({exitcode}) does not exists")
        return f"{excode[0]['id']}: {excode[0]['desc']}{detail}"
    else:
        logging.error("Unexpected type for parameter 'exitcode'. Allowed: int")
        return None


def warning(exitcode, detail=None):
    logging.error(stringify_exitcode(exitcode, detail))


class ProbePositive(Exception):
    def __init__(self, detail, kill=True):
        logging.error(
            """0:The modules for the specified file indicates positive (obfuscation technique applied). """ + detail)
        if kill:
            exit(0)


class ProbeNegative(Exception):
    def __init__(self, detail, kill=True):
        logging.error(
            """1:The modules for the specified file indicates negative (obfuscation technique not applied). """ + detail)
        if kill:
            exit(1)


class ProbeFail(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""2:The modules could not be completed due to an unexpected error. """ + detail)
        if kill:
            exit(2)


class ProbeUndetermined(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""3:The modules for the specified file is undetermined (result not 100% sure). """ + detail)
        if kill:
            exit(3)


class FileNotFound(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""101:File/directory not found or not enough permissions. """ + detail)
        if kill:
            exit(101)


class NotAnElf(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""102:Specified file is not an ELF. """ + detail)
        if kill:
            exit(102)


class TemplateNotFound(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""103:template not found. """ + detail)
        if kill:
            exit(103)


class OutWriterError(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""104:Template extension and report extension do not match. """ + detail)
        if kill:
            exit(104)


class FilterError(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""105:Invalid filter, only Probe ID allowed. """ + detail)
        if kill:
            exit(105)


class ReportFail(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""106:Report generation failed. """ + detail)
        if kill:
            exit(106)


class ExecutionSuccess(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""200:Program execution successful. """ + detail)
        if kill:
            exit(200)


class ExecutionFail(Exception):
    def __init__(self, detail, kill=True):
        logging.error("""201:Program execution failed. """ + detail)
        if kill:
            exit(201)
