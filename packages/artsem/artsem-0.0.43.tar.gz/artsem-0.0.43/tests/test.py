import sys


class DataframeDict(dict):

    def __init__(self):
        super().__init__()

    def update(self, *args, **kwargs):
        print("soy yo soy yo")
        for arg in args:
            assert isinstance(arg, dict), f"Invalid type. Expected dict, obtained {type(arg)}"
            for k, v in arg.items():
                assert isinstance(v, str) and isinstance(k, str), \
                    f"Invalid type. Expected string: pandas.DataFrame, obtained {type(k)}: {type(v)}"
        for k, v in kwargs:
            assert isinstance(v, str) and isinstance(k, str), \
                f"Invalid type. Expected string: pandas.DataFrame, obtained {type(k)}: {type(v)}"
        super().update(*args, **kwargs)



def _parse_args():
    import argparse

    parser = argparse.ArgumentParser(description="Obfuscation analyzer for ELF binaries")
    parser.add_argument("target", help="ELF file (single analysis) or ELF Directory (batch analysis)",
                        type=str)
    parser.add_argument("-v", action="count", default=0, help="increase output verbosity [-v, -vv, -vvv]")
    parser.add_argument("-o", type=str, help="File to write the output")

    ck_group = parser.add_mutually_exclusive_group()
    ck_group.add_argument("--check", type=int, metavar="CK_ID", nargs="+",
                          help="Only specified CecKs (IDs) are executed")
    ck_group.add_argument("--exclude", type=int, metavar="CK_ID", nargs="+",
                          help="Specified ChecKs (IDs) are excluded; the rest are executed")
    return parser.parse_args()


# args = parse_args()
__args__ = sys.argv
print(f'ARGS: {__args__}')

a = DataframeDict()
b = {'apellido': 'bombo'}
a.update({'nombre': 'manolo'})
a.update({'nombre': 5})
a.update(b)
print(a)
