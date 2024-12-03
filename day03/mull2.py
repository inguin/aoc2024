#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0
enabled = True

with open(filename) as f:
    for line in f:
        for m in re.finditer(r"mul\(([0-9]+),([0-9]+)\)|do\(\)|don't\(\)", line):
            if m[0] == "do()":
                enabled = True
            elif m[0] == "don't()":
                enabled = False
            elif enabled:
                total += int(m[1]) * int(m[2])
print(total)
