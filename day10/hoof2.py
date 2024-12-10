#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(filename) as f:
    for line in f:
        grid.append([ int(n) for n in line.strip() ])

def get_score(row, col, height):
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]):
        return 0
    if grid[row][col] != height:
        return 0
    if height == 9:
        return 1
    return (get_score(row - 1, col, height + 1) +
            get_score(row + 1, col, height + 1) +
            get_score(row, col - 1, height + 1) +
            get_score(row, col + 1, height + 1))

total = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        total += get_score(row, col, 0)

print(total)
