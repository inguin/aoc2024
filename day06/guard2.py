#! /usr/bin/python

import sys

North = (0, -1)
East = (1, 0)
South = (0, 1)
West = (-1, 0)

def isloop(grid, newx, newy, guardpos):
    newgrid = []
    for y, line in enumerate(grid):
        newline = ''
        for x, c in enumerate(line):
            newline += ('#' if x == newx and y == newy else c)
        newgrid.append(newline)
    grid = newgrid

    guarddir = North
    path = set()

    while (guardpos, guarddir) not in path:
        path.add((guardpos, guarddir))
        nextpos = (guardpos[0] + guarddir[0], guardpos[1] + guarddir[1])
        if nextpos[0] < 0 or nextpos[1] < 0:
            return False
        try:
            if grid[nextpos[1]][nextpos[0]] == '.':
                guardpos = nextpos
                continue
        except IndexError:
            return False
        if guarddir == North: guarddir = East
        elif guarddir == East: guarddir = South
        elif guarddir == South: guarddir = West
        else: guarddir = North

    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            ns = ((x, y), North) in path or ((x, y), South) in path
            ew = ((x, y), East) in path or ((x, y), West) in path
            if ns and ew:
                print('+', end='')
            elif ns:
                print('|', end='')
            elif ew:
                print('-', end='')
            else:
                print(c, end='')
        print()

    return True

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = [ line.strip() for line in open(filename) ]

for y, line in enumerate(grid):
    if (x := line.find('^')) >= 0:
        grid[y] = line.replace('^', '.')
        guardpos = (x, y)

count = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if (x, y)  == guardpos:
            continue
        if isloop(grid, x, y, guardpos):
            print(f"obstacle at ({x}, {y}) creates a loop")
            count += 1

print(count)
