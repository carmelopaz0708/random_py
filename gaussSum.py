#!/usr/bin/env python3

# gaussSum.py
# Obtain the total sum of all numbers from zero to x

import sys

def main():
    total = 0

    try:
        var = int(input("$ "))

    except ValueError:
        print("Invalid Input")
        sys.exit(1)

    if var % 2 == 0:
        total = (var // 2) * (var + 1)

    else:
        total = ((var + 1) // 2) * var

    print("[0 ... {}] = {}".format(var, total))
    sys.exit(0)


if __name__ == "__main__":
    main()