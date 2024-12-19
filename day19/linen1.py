#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    towels = [ towel.strip() for towel in f.readline().split(',') ]
    f.readline()
    patterns = [ pattern.strip() for pattern in f.readlines() ]

def pattern_possible(pattern):
    if pattern in towels:
        return True
    return any(pattern.startswith(towel) and pattern_possible(pattern.removeprefix(towel)) for towel in towels)

print(sum(pattern_possible(pattern) for pattern in patterns))
