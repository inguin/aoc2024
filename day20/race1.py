#! /usr/bin/python

import sys
from collections import namedtuple

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []
Position = namedtuple('Position', ('x', 'y'))

with open(filename) as f:
    for y, line in enumerate(f):
        if 'S' in line:
            start = Position(line.index('S'), y)
        if 'E' in line:
            end = Position(line.index('E'), y)
        grid.append(line.strip().replace('S', '.').replace('E', '.'))

height = len(grid)
width = len(grid[0])

distances = [ [None] * width for _ in range(height) ]
pos = start
distance = 0
path = []

while pos != end:
    path.append(pos)
    distances[pos.y][pos.x] = len(path)
    for nextpos in (Position(pos.x - 1, pos.y), Position(pos.x + 1, pos.y),
                    Position(pos.x, pos.y - 1), Position(pos.x, pos.y + 1)):
        if (nextpos.x in range(width) and nextpos.y in range(height) and
            grid[nextpos.y][nextpos.x] == '.' and distances[nextpos.y][nextpos.x] is None):
            pos = nextpos
            break

path.append(end)
distances[end.y][end.x] = len(path)

cheats = 0

for pos in path:
    for cheatpos in (Position(pos.x - 2, pos.y), Position(pos.x + 2, pos.y),
                     Position(pos.x, pos.y - 2), Position(pos.x, pos.y + 2)):
        if (cheatpos.x in range(width) and cheatpos.y in range(height) and
            distances[cheatpos.y][cheatpos.x] is not None):
            saved = distances[cheatpos.y][cheatpos.x] - distances[pos.y][pos.x] - 2
            if saved >= 100:
                cheats += 1

print(cheats)
