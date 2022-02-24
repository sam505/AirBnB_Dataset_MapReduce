#!/usr/bin/python3 -O

import sys


def main():
    """
    input comes from STDIN
    :return:
    """
    lines = 0
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        values, ideal_count = line.split('\t')
        if len(values.split(",")) == int(ideal_count):
            lines += 1

    print(f"Total number of good lines in AirBNB file: {lines}")


if __name__ == "__main__":
    main()
