#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

def is_safe(levels):
    diff1 = levels[0] - levels[1]
    if diff1 == 0:
        return False
    for l1, l2 in zip(levels, levels[1:]):
        diff2 = l1 - l2
        if diff1 < 0 and (diff2 < -3 or diff2 > -1):
            return False
        if diff1 > 0 and (diff2 < 1 or diff2 > 3):
            return False
    return True

result = 0
with open(filename) as f:
    for line in f:
        levels = [ int(t) for t in line.split() ]
        if is_safe(levels):
            result += 1
        elif any(is_safe(levels[:n] + levels[n+1:]) for n in range(len(levels))):
            result += 1
print(result)
