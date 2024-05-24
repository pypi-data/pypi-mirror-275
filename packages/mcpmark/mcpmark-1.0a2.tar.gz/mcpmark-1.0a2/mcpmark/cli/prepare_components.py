#!/usr/bin/env python
""" Prepare components for marking

* Rewrite component notebooks into their own directories.
* Make Rmd versions of notebooks.
"""

import os
import os.path as op
import re
from pathlib import Path
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import shutil
import warnings

import jupytext
import pandas as pd

from ..mcputils import (read_config, get_minimal_df, get_notebooks,
                       component_path, MCPError, has_md_checker)


def get_component_nbs(in_dir, component_tests):
    notebooks = get_notebooks(in_dir, recursive=True)
    component_nbs = {}
    for nb_fname in notebooks:
        nb = jupytext.read(nb_fname)
        for component, component_test in component_tests.items():
            if component_test(nb, nb_fname):
                if component in component_nbs:
                    prev_nb = component_nbs[component][0]
                    raise MCPError(
                        f'Found second nb "{nb_fname}"; first was "{prev_nb}"')
                component_nbs[component] = (nb_fname, nb)
    missing = set(component_tests).difference(component_nbs)
    if missing:
        missing = '\n'.join(sorted(missing))
        raise MCPError(f'Missing notebooks in {in_dir}:\n{missing}')
    return component_nbs


def get_component_tests(config):
    # component_scrip_path overrides regex in components.
    if (csp := config.get('component_script_path')):
        return comp_tests_from_script(Path(csp))
    # Should be on regex in each component
    tests = {}
    for name, info in config['components'].items():
        if not 'regex' in info:
            raise MCPError(
                'Need either component_script_path or regex field '
                'for each component')
        tests[name] = has_md_checker(info['regex'],
                                     flags=re.I | re.MULTILINE)
    return tests


def comp_tests_from_script(c_script_path):
    ns = {}
    exec(c_script_path.read_text(), ns)
    return ns['COMPONENT_TESTS']



def expected_student_dirs(config, drop_missing=False):
    df = get_minimal_df(config)
    stid_col = config['student_id_col']
    known_submitters = config.get('known_submitters', [])
    known_missing = config.get('known_missing', [])
    # These are students known to have no IDs, and who therefore must
    # be missing.
    no_ids = config.get('no_ids', {})
    other_id_col = no_ids.get('other_id_col')
    no_id_students = no_ids.get('students', [])
    dir_names = []
    for i_val, row in df.iterrows():
        student_id = row.loc[stid_col]
        if pd.isna(student_id):
            if drop_missing:
                warnings.warn(f'Missing identifier for {row}')
                continue
            if other_id_col and row[other_id_col] in no_id_students:
                continue
            raise RuntimeError(
                f'Student id missing for col "{stid_col}": row: {row}')
        if known_submitters and student_id not in known_submitters:
            continue
        if student_id in known_missing:
            continue
        if student_id in dir_names:
            raise RuntimeError(f'Duplicate student id: "{student_id}"')
        dir_names.append(student_id)
    return dir_names


def create_dirs(root_path, names, gitignore=False):
    for name in names:
        out_path = op.join(root_path, name)
        if not op.isdir(out_path):
            os.makedirs(out_path)
            if gitignore:
                with open(op.join(out_path, '.gitignore'), 'wt') as fobj:
                    fobj.write('')


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('--config-path',
                        default=op.join(os.getcwd(), 'assign_config.yaml'),
                        help='Path to config file')
    parser.add_argument('--out-path',
                        help='Path for output directories')
    parser.add_argument(
        '--drop-missing', action='store_true',
        help='If set, drop missing rows with missing student identifier')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    if args.out_path is None:
        args.out_path = op.dirname(args.config_path)
    config = read_config(args.config_path)
    component_tests = get_component_tests(config)
    component_names = list(component_tests)
    component_base = component_path(config)
    create_dirs(component_base, component_names)
    sub_path = config['submissions_path']
    for login_id in expected_student_dirs(config, args.drop_missing):
        exp_path = op.join(sub_path, login_id)
        if not op.isdir(exp_path):
            raise RuntimeError(f'{exp_path} expected, but does not exist')
        nbs = get_component_nbs(exp_path, component_tests)
        for component, (nb_fname, nb) in nbs.items():
            component_root = op.join(component_base, component)
            _, ext = op.splitext(nb_fname)
            out_root = op.join(component_root, login_id)
            shutil.copy2(nb_fname, out_root + ext)
            if ext.lower() != '.rmd':  # Write Rmd version if necessary.
                jupytext.write(nb, out_root + '.Rmd', fmt='Rmd')
            create_dirs(component_root,
                        ['marking'],
                        gitignore=True)


if __name__ == '__main__':
    main()
