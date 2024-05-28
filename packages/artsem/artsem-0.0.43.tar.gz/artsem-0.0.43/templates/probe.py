#!/usr/bin/env python3
from os.path import dirname
import artsemLib

if __name__ == '__main__':
    args = artsemLib.Probe(dirname(__file__)).parse_cli()
    # Do your magic here.
    # TODO: implement the modules
    exit(100)
