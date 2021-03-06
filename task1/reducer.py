#!/usr/bin/python3 -O

import sys

# maps neighborhoods to their counts
neighborhoods_count = {}


def main():
    """
    input comes from STDIN
    :return:
    """
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()

        # parse the input we got from mapper.py
        try:
            neighborhood_group, neighborhood, count = line.split('\t', 2)
            # convert count (currently a string) to int
            count = int(count)
            try:
                neighborhoods_count[neighborhood_group + " " + neighborhood] += count
            except KeyError:
                neighborhoods_count[neighborhood_group + " " + neighborhood] = count
        except ValueError:
            pass

    # write the results to stdout
    for neighborhoods in neighborhoods_count:
        print('%s\t%s' % (neighborhoods, neighborhoods_count[neighborhoods]))


if __name__ == "__main__":
    main()
