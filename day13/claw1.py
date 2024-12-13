#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    lines = f.readlines()

def cheapest(veca, vecb, prize):
    mincost = None
    for a in range(0, 100):
        for b in range(0, 100):
            if (a * veca[0] + b * vecb[0] == prize[0] and
                a * veca[1] + b * vecb[1] == prize[1] and
                (mincost is None or 3 * a + b < mincost)):
                mincost = 3 * a + b
    return mincost or 0

total = 0

while lines:
    m = re.match(r'.*X\+(\d+), Y\+(\d+)', lines[0])
    veca = (int(m[1]), int(m[2]))
    m = re.match(r'.*X\+(\d+), Y\+(\d+)', lines[1])
    vecb = (int(m[1]), int(m[2]))
    m = re.match(r'.*X=(\d+), Y=(\d+)', lines[2])
    prize = (int(m[1]), int(m[2]))
    lines = lines[4:]
    total += cheapest(veca, vecb, prize)

print(total)
