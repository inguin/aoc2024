#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = open(filename).read().splitlines()

def get_char(x, y):
    if y < 0 or y >= len(grid):
        return None
    if x < 0 or x >= len(grid[y]):
        return None
    return grid[y][x]

def is_xmas(x, y):
    a = get_char(x, y)
    ne = get_char(x + 1, y - 1)
    se = get_char(x + 1, y + 1)
    sw = get_char(x - 1, y + 1)
    nw = get_char(x - 1, y - 1)
    return (a == 'A' and
            (ne == 'M' and sw == 'S' or ne == 'S' and sw == 'M') and
            (se == 'M' and nw == 'S' or se == 'S' and nw == 'M'))

count = 0
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if is_xmas(x, y):
            count += 1
print(count)
