#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
line = open(filename).read().strip()

gap = False
blocks = []
fileid = 0

for digit in line:
    if not gap:
        blocks += [fileid] * int(digit)
    else:
        blocks += [None] * int(digit)
        fileid += 1
    gap = not gap

i = 0

while i < len(blocks):
    if blocks[i] is None:
        blocks[i] = blocks.pop()
    i += 1
    while blocks[-1] is None:
        blocks.pop()

checksum = sum(i * fileid for i, fileid in enumerate(blocks))
print(checksum)
