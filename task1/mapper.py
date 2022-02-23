#!/usr/bin/python3 -O
import sys

index = []


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
            [index.append(value) for value in values]

        count += 1

        # print values to stdout
        print('%s\t%s\t%s' % (values[index.index("UNIQUE_CARRIER_NAME")], values[index.index("DEST")-len(index)], "1"))


if __name__ == "__main__":
    main()
