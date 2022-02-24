#!/usr/bin/python3 -O

import sys

# maps neighborhoods to their counts


def main():
    lines = 0
    """
    input comes from STDIN
    :return:
    """
    for line in sys.stdin:
        # increment count
        lines += 1
    print(f"Total number of lines in AirBNB file: {lines}")


if __name__ == "__main__":
    main()
