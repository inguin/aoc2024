#! /usr/bin/python

import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def count_after_blinks(pebble, blinks):
    if blinks == 0:
        return 1

    if pebble == "0":
        return count_after_blinks("1", blinks - 1)

    if len(pebble) % 2 == 0:
        left = str(int(pebble[:len(pebble)//2]))
        right = str(int(pebble[len(pebble)//2:]))
        return count_after_blinks(left, blinks - 1) + count_after_blinks(right, blinks - 1)

    return count_after_blinks(str(int(pebble) * 2024), blinks - 1)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(filename) as f:
    pebbles = f.read().split()

print(sum(count_after_blinks(pebble, 75) for pebble in pebbles))
