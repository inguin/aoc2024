#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    lines = f.readlines()

def cheapest(veca, vecb, prize):
    a = round((prize[1] - prize[0] * vecb[1] / vecb[0]) / (veca[1] - veca[0] * vecb[1] / vecb[0]))
    b = round((prize[1] - prize[0] * veca[1] / veca[0]) / (vecb[1] - vecb[0] * veca[1] / veca[0]))

    if (a * veca[0] + b * vecb[0] == prize[0] and a * veca[1] + b * vecb[1] == prize[1]):
        return 3 * a + b
    return 0

total = 0

while lines:
    m = re.match(r'.*X\+(\d+), Y\+(\d+)', lines[0])
    veca = (int(m[1]), int(m[2]))
    m = re.match(r'.*X\+(\d+), Y\+(\d+)', lines[1])
    vecb = (int(m[1]), int(m[2]))
    m = re.match(r'.*X=(\d+), Y=(\d+)', lines[2])
    prize = (10000000000000 + int(m[1]), 10000000000000 + int(m[2]))
    lines = lines[4:]
    total += cheapest(veca, vecb, prize)

print(total)
