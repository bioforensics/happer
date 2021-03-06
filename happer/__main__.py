#!/usr/bin/env python3
#
# -----------------------------------------------------------------------------
# Copyright (c) 2018, Battelle National Biodefense Institute.
#
# This file is part of happer (http://github.com/bioforensics/happer) and is
# licensed under the BSD license: see LICENSE.txt.
# -----------------------------------------------------------------------------

import argparse
import happer
import sys


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', action='version',
                        version='happer v{}'.format(happer.__version__))
    parser.add_argument('-o', '--out', metavar='FILE', default='-',
                        help='write haplotype sequences to the specified '
                        'file; default is the terminal (stdout)')
    parser.add_argument('seqfile', help='input sequences in Fasta format')
    parser.add_argument('bed', help='haplotypes annotated in BED format')
    return parser


def main(args=None):
    """Entry point for the happer CLI.

    Isolated as a method so that the CLI can be called by other Python code
    (e.g. for testing), in which case the arguments are passed to the function.
    If no arguments are passed to the function, parse them from the command
    line.
    """
    if args is None:  # pragma: no cover
        if len(sys.argv) == 1:
            get_parser().parse_args(['-h'])
        args = get_parser().parse_args()

    versionmessage = '[happer] running version {}'.format(happer.__version__)
    print(versionmessage, file=sys.stderr)
    happer.mutate.main(args)
