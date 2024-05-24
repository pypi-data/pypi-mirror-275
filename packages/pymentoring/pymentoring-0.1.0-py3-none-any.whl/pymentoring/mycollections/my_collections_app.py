import argparse
import os

from pymentoring.mycollections.my_collections import get_unique_chars


def create_parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-s', '--string', type=str, help='String to process')
    parser.add_argument('-f', '--file', type=str, help='Path to text file to process')
    return parser


def process_file(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    yield line.replace("\n", "")
        except Exception as e:
            print(e)
    else:
        print(f'File {file_path} not found')


def file_mode_handler(file_path) -> bool:
    accum: set[str] = set([])
    for chars in process_file(file_path):
        chars_set = set(chars)
        accum = (accum - chars_set).union(chars_set - accum)
    sorted_accum = list(accum)
    sorted_accum.sort()
    print_unique_chars(sorted_accum)
    return True


def string_mode_handler(text) -> bool:
    print_unique_chars(get_unique_chars(text))
    return True


def print_unique_chars(chars: list[str]):
    print(f'characters [{", ".join(chars)}] are presented once')


def process_args(args, f_handler=file_mode_handler, s_handler=string_mode_handler):
    if args.file:
        return f_handler(args.file)
    elif args.string:
        return s_handler(args.string)
    return False


def main(parser):
    return process_args(parser.parse_args())


if __name__ == "__main__":
    argParser = create_parser()
    if not main(argParser):
        argParser.print_help()
