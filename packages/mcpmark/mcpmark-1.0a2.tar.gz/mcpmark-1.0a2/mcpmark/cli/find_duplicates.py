#!/usr/bin/env python
""" Print duplicate files
"""

import sys
from hashlib import sha1
from collections import defaultdict
from argparse import ArgumentParser, RawDescriptionHelpFormatter

def shasum(fname):
    with open(fname, 'rb') as fobj:
        return sha1(fobj.read()).hexdigest()

def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('fnames', nargs='+',
                        help='Notebook filenames')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    duplicates = defaultdict(list)
    for fn in args.fnames:
        sha = shasum(fn)
        duplicates[sha].append(fn)
    clusters = [(k, v) for k, v in duplicates.items() if len(v) > 1]
    for key, cluster in clusters:
        print(f'Cluster {key[:7]}:')
        print('  ' + '\n  '.join(cluster))


if __name__ == '__main__':
    main()
