#! /usr/bin/python

import sys
from collections import namedtuple

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

Vec = namedtuple("Vec", ("x", "y"))
North = Vec(0, -1)
East = Vec(1, 0)
South = Vec(0, 1)
West = Vec(-1, 0)

grid = []
instructions = ""

with open(filename) as f:
    for y, line in enumerate(f):
        line = line.strip()
        if not line:
            break
        tiles = list(line)
        if '@' in tiles:
            x = tiles.index('@')
            robot = Vec(x, y)
        grid.append(list(line))

    for line in f:
        instructions += line.strip()

def move(x, y, direction):
    c = grid[y + direction.y][x + direction.x]
    if c == '.':
        grid[y + direction.y][x + direction.x] = grid[y][x]
        grid[y][x] = '.'
        return True
    elif c == 'O' and move(x + direction.x, y + direction.y, direction):
        grid[y + direction.y][x + direction.x] = grid[y][x]
        grid[y][x] = '.'
        return True
    return False

for instruction in instructions:
    print("Move", instruction)
    if instruction == '^': direction = North
    elif instruction == '>': direction = East
    elif instruction == 'v': direction = South
    elif instruction == '<': direction = West

    if move(robot.x, robot.y, direction):
        robot = Vec(robot.x + direction.x, robot.y + direction.y)

    for line in grid:
        for c in line:
            print(c, end='')
        print()

total = 0

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if grid[y][x] == 'O':
            total += 100 * y + x

print(total)
