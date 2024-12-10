#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(filename) as f:
    for line in f:
        grid.append([ int(n) for n in line.strip() ])

def get_trailheads(row, col, height):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
        return []
    if grid[row][col] != height:
        return []
    if height == 9:
        return [(row, col)]
    return (get_trailheads(row - 1, col, height + 1) +
            get_trailheads(row + 1, col, height + 1) +
            get_trailheads(row, col - 1, height + 1) +
            get_trailheads(row, col + 1, height + 1))

total = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        trailheads = set(get_trailheads(row, col, 0))
        total += len(trailheads)

print(total)
