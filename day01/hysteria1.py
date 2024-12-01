#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

in1 = []
in2 = []

with open(filename) as f:
    for line in f:
        a, b = line.split()
        in1.append(int(a))
        in2.append(int(b))

total = 0
for a, b in zip(sorted(in1), sorted(in2)):
    total += abs(a - b)
print(total)
