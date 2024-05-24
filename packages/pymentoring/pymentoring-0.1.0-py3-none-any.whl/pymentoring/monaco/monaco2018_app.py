import os

from pymentoring.monaco.monaco2018 import Monaco2018


def main():
    monaco = Monaco2018()
    print(monaco.build_table())


if __name__ == "__main__":
    main()
