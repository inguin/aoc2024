#! /usr/bin/python

import sys
from functools import lru_cache

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    towels = [ towel.strip() for towel in f.readline().split(',') ]
    f.readline()
    patterns = [ pattern.strip() for pattern in f.readlines() ]

@lru_cache(maxsize=None)
def pattern_combinations(pattern):
    if not pattern:
        return 1
    return sum(pattern_combinations(pattern.removeprefix(towel))
               for towel in towels if pattern.startswith(towel))

print(sum(pattern_combinations(pattern) for pattern in patterns))
