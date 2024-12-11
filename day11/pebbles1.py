#! /usr/bin/python

import sys

def blink(pebbles):
    for i, item in enumerate(pebbles):
        if isinstance(item, list):
            blink(item)
        elif item == "0":
            pebbles[i] = "1"
        elif len(item) % 2 == 0:
            left = str(int(item[:len(item)//2]))
            right = str(int(item[len(item)//2:]))
            pebbles[i] = [ left, right ]
        else:
            pebbles[i] = str(int(item) * 2024)

def count(pebbles):
    return sum(count(item) if isinstance(item, list) else 1 for item in pebbles)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(filename) as f:
    pebbles = f.read().split()

for _ in range(25):
    blink(pebbles)

print(count(pebbles))
