#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0

with open(filename) as f:
    for line in f:
        for m in re.finditer(r"mul\(([0-9]+),([0-9]+)\)", line):
            total += int(m[1]) * int(m[2])
print(total)
