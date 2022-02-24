#!/usr/bin/python3 -O

import sys

idx = []


def main():
    """
    gets all lines from stdin
    :return:
    """
    count = 0
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # split the line into individual values
        values = line.split(",")
        if count == 0:
            [idx.append(value) for value in values]

        count += 1

        # print values to stdout
        try:
            print('%s\t%s\t%s' % (values[idx.index("neighbourhood_group")], values[idx.index("neighbourhood")], "1"))
        except IndexError:
            pass


if __name__ == "__main__":
    main()
