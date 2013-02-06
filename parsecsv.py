#!/usr/bin/env python

import argparse
import csv
import itertools
import sys
from argx.default import default_arg


def csv_to_fields(istream, ostream, delim, skip):
    """
    Write CSV data from `istream` to `ostream` using `delim` as the field delimiter.
    """
    reader = csv.reader(istream)
    if skip > 0:
        reader = itertools.islice(reader, skip, None)
    for row in reader:
        ostream.write(delim.join(row))
        ostream.write('\n')


def main():
    argparser = argparse.ArgumentParser(description = 'Parse a CSV file')
    argparser.add_argument(
            'filename', nargs = '?',
            help = 'The input filename; use standard input if missing',
            metavar = 'file.csv')
    argparser.add_argument(
            '-d', '--delim', default = '\t',
            help = 'Use DELIM as the filed delimiter instead of the tab character')
    argparser.add_argument(
            '-s', '--skip', default = 0, nargs = '?', type = int,
            action = default_arg(1),
            help = 'Skip N lines; if N is unspecified, it defaults to 1',
            metavar = 'N')

    args = argparser.parse_args()

    istream = open(args.filename, 'rb') if args.filename is not None else sys.stdin
    ostream = sys.stdout

    try:
        csv_to_fields(istream, ostream, args.delim, args.skip)
    finally:
        if args.filename is not None:
            istream.close()


if __name__ == '__main__':
    sys.exit(main())
