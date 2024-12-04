#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = open(filename).read().splitlines()
North = (0, -1)
NorthEast = (1, -1)
East = (1, 0)
SouthEast = (1, 1)
South = (0, 1)
SouthWest = (-1, 1)
West = (-1, 0)
NorthWest = (-1, -1)
Directions = (North, NorthEast, East, SouthEast, South, SouthWest, West, NorthWest)

def get_char(pos):
    x, y = pos
    if y < 0 or y >= len(grid):
        return None
    if x < 0 or x >= len(grid[y]):
        return None
    return grid[y][x]

def step(pos, direction, steps):
    return ((pos[0] + direction[0] * steps), (pos[1] + direction[1] * steps))

def is_xmas(pos, direction):
    return (get_char(pos) == 'X' and
            get_char(step(pos, direction, 1)) == 'M' and
            get_char(step(pos, direction, 2)) == 'A' and
            get_char(step(pos, direction, 3)) == 'S')

def count_xmas_by_dir(direction):
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if is_xmas((x, y), direction):
                count += 1
    print(f"{direction}: {count} instances")
    return count

print(sum(count_xmas_by_dir(direction) for direction in Directions))
