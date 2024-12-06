#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = [ line.strip() for line in open(filename) ]

North = (0, -1)
East = (1, 0)
South = (0, 1)
West = (-1, 0)

for y, line in enumerate(grid):
    if (x := line.find('^')) >= 0:
        grid[y] = line.replace('^', '.')
        guardpos = (x, y)
        guarddir = North

path = []

while (guardpos, guarddir) not in path:
    path.append((guardpos, guarddir))
    nextpos = (guardpos[0] + guarddir[0], guardpos[1] + guarddir[1])
    try:
        if grid[nextpos[1]][nextpos[0]] == '.':
            guardpos = nextpos
            continue
    except IndexError:
        break
    if guarddir == North: guarddir = East
    elif guarddir == East: guarddir = South
    elif guarddir == South: guarddir = West
    else: guarddir = North

visited = set(item[0] for item in path)
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if (x, y) in visited:
            print('*', end='')
        else:
            print(grid[y][x], end='')
    print()

print(len(visited))
