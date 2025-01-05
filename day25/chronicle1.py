#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    lines = [ line.strip() for line in f ]

locks = []
keys = []

while lines:
    pins = [ sum(lines[row][col] == '#' for row in range(1, 6)) for col in range(5) ]
    if lines[0][0] == '#':
        locks.append(pins)
    else:
        keys.append(pins)
    lines = lines[8:]

result = 0

for lock in locks:
    for key in keys:
        pins = [ l + k for l, k in zip(lock, key) ]
        if all(pin <= 5 for pin in pins):
            result += 1

print(result)
