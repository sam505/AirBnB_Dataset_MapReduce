#!/usr/bin/python3 -O

import sys

idx = []


def main():
    """
    gets all lines from stdin
    :return:
    """
    file = open("response.txt", "w")
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        print(f"{line}\t1")
        file.write(f"{line}\n")
    file.close()


if __name__ == "__main__":
    main()
