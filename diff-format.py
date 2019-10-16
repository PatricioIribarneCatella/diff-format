#!/usr/bin/env python3

from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from diff import Diff

def main(diff_file, output_file):

    IGNORE = ["GNUmakefile", ".gitignore", "gradelib.py", "grade-lab2"]
    
    d = Diff(diff_file, IGNORE)
    d.export(output_file)

if __name__ == "__main__":

    parser = ArgumentParser(
                    description='DIFF-PARSER',
                    formatter_class=ArgumentDefaultsHelpFormatter)
    
    parser.add_argument(
            '--diff',
            default='out.diff',
            help='Diff formated file'
    )

    parser.add_argument(
            '--output',
            help='Output parsed file'
    )

    args = parser.parse_args()
 
    main(args.diff, args.output)

