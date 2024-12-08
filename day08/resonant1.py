#! /usr/bin/python

import collections, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(filename) as f:
    lines = [ line.strip() for line in f.readlines() ]

antennas = collections.defaultdict(list)

for row, line in enumerate(lines):
    for col, char in enumerate(line.strip()):
        if char != '.':
            antennas[char].append((row, col))

antinodes = set()

for char, positions in antennas.items():
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            a1 = (2 * positions[i][0] - positions[j][0], 2 * positions[i][1] - positions[j][1])
            a2 = (2 * positions[j][0] - positions[i][0], 2 * positions[j][1] - positions[i][1])
            if a1[0] >= 0 and a1[0] < len(lines) and a1[1] >= 0 and a1[1] < len(lines[0]):
                antinodes.add(a1)
            if a2[0] >= 0 and a2[0] < len(lines) and a2[1] >= 0 and a2[1] < len(lines[0]):
                antinodes.add(a2)

for row, line in enumerate(lines):
    for col, char in enumerate(line):
        if char == '.' and (row, col) in antinodes:
            print('#', end='')
        else:
            print(char, end='')
    print()

print(len(antinodes))
