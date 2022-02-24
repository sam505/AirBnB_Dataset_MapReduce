#!/usr/bin/python3 -O

import sys


def main():
    """
    gets all lines from stdin
    :return:
    """
    file = open("response.txt", "w")
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
            print(f"{line}\t{ideal_len}")
            file.write(f"{line}\t{ideal_len}\n")
    file.close()


if __name__ == "__main__":
    main()
