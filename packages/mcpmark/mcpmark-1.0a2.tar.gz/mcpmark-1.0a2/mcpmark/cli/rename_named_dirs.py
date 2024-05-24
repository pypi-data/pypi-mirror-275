#!/usr/bin/env python
""" Rename directories passed on command line to login names
"""

import os
import os.path as op
import shutil
from argparse import ArgumentParser, RawDescriptionHelpFormatter

from ..mcputils import read_config, dirs2logins


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('dir_names', nargs='+',
                        help='Directories to rename to login')
    parser.add_argument('--config-path',
                        default=op.join(os.getcwd(), 'assign_config.yaml'),
                        help='Path to config file')
    parser.add_argument('--clobber', action='store_true',
                        help='If set, delete existing output directories')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    config = read_config(args.config_path)
    lookup = dirs2logins(config)
    for d in args.dir_names:
        d_path, d_name = op.split(d)
        if d_name not in lookup:
            print(f'Directory/filename {d} not in lookup')
            continue
        out_path = op.join(d_path, lookup[d_name])
        if op.isdir(out_path) and not args.clobber:
            raise RuntimeError(f'{out_path} exists and --clobber not set')
        print(f'Moving {d} to {out_path}')
        shutil.move(d, out_path)


if __name__ == '__main__':
    main()
