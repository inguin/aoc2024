#! /usr/bin/python

import sys
from collections import Counter

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

in1 = []
in2 = []

with open(filename) as f:
    for line in f:
        a, b = line.split()
        in1.append(int(a))
        in2.append(int(b))

in2_counts = Counter(in2)

total = 0
for a in in1:
    total += a * in2_counts[a]
print(total)
