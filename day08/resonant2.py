#! /usr/bin/python

import collections, math, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(filename) as f:
    lines = [ line.strip() for line in f.readlines() ]

def in_grid(pos):
    row, col = pos
    return row >= 0 and row < len(lines) and col >= 0 and col < len(lines[0])

antennas = collections.defaultdict(list)

for row, line in enumerate(lines):
    for col, char in enumerate(line.strip()):
        if char != '.':
            antennas[char].append((row, col))

antinodes = set()

for char, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            rowdist = positions[i][0] - positions[j][0]
            coldist = positions[i][1] - positions[j][1]
            gcd = math.gcd(rowdist, coldist)
            rowdist //= gcd
            coldist //= gcd

            n = 0
            while in_grid(a := (positions[i][0] + n * rowdist, positions[i][1] + n * coldist)):
                antinodes.add(a)
                n += 1
            n = -1
            while in_grid(a := (positions[i][0] + n * rowdist, positions[i][1] + n * coldist)):
                antinodes.add(a)
                n -= 1

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '.' and (row, col) in antinodes:
            print('#', end='')
        else:
            print(char, end='')
    print()

print(len(antinodes))
