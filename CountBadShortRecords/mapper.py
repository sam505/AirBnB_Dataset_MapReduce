#!/usr/bin/python3 -O

import sys

idx = []


def main():
    """
    gets all lines from stdin
    :return:
    """
    file = open("response.txt", "w")
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
        print(f"{values}\t{len(idx)}")
        file.write(f"{values}\t{len(idx)}\n")
    file.close()


if __name__ == "__main__":
    main()
