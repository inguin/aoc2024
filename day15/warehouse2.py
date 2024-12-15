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
        tiles = []
        for c in line:
            if c == 'O':
                tiles += [ '[', ']' ]
            elif c == '@':
                tiles += [ '@', '.' ]
            else:
                tiles += [ c, c ]
        if '@' in tiles:
            x = tiles.index('@')
            robot = Vec(x, y)
        grid.append(tiles)

    for line in f:
        instructions += line.strip()

def canmove(x, y, direction):
    c = grid[y + direction.y][x + direction.x]
    if c == '.':
        return True
    if c == '[':
        return (canmove(x + direction.x, y + direction.y, direction) and
                (direction in (East, West) or canmove(x + direction.x + 1, y + direction.y, direction)))
    if c == ']':
        return (canmove(x + direction.x, y + direction.y, direction) and
                (direction in (East, West) or canmove(x + direction.x - 1, y + direction.y, direction)))
    else:
        return False

def move(x, y, direction):
    c = grid[y][x]
    if grid[y + direction.y][x + direction.x] != '.':
        move(x + direction.x, y + direction.y, direction)

    if direction in (North, South):
        if c == '[' and grid[y + direction.y][x + 1] != '.':
            move(x + 1, y + direction.y, direction)
        elif c == ']' and grid[y + direction.y][x - 1] != '.':
            move(x - 1, y + direction.y, direction)

    grid[y + direction.y][x + direction.x] = grid[y][x]
    grid[y][x] = '.'

    if direction in (North, South):
        if c == '[':
            grid[y + direction.y][x + 1] = grid[y][x + 1]
            grid[y][x + 1] = '.'
        elif c == ']':
            grid[y + direction.y][x - 1] = grid[y][x - 1]
            grid[y][x - 1] = '.'

for instruction in instructions:
    print("Move", instruction)
    if instruction == '^': direction = North
    elif instruction == '>': direction = East
    elif instruction == 'v': direction = South
    elif instruction == '<': direction = West

    if canmove(robot.x, robot.y, direction):
        move(robot.x, robot.y, direction)
        robot = Vec(robot.x + direction.x, robot.y + direction.y)

    for line in grid:
        for c in line:
            print(c, end='')
        print()

total = 0

for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if grid[y][x] == '[':
            total += 100 * y + x

print(total)
