#!/usr/bin/python3 -O

import sys


def main():
    """
    gets all lines from stdin
    :return:
    """
    status = True
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        if status:
            values = line.split(",")
            ideal_len = len(values)
            status = False
        else:
            # print values to stdout
            print(f"0{line}\t{ideal_len}")


if __name__ == "__main__":
    main()
