#! /usr/bin/python

import re, sys, time
from collections import namedtuple

Width = 101
Height = 103

Robot = namedtuple('Robot', ('x', 'y', 'dx', 'dy'))
robots = []

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    for line in f:
        x, y, dx, dy = re.findall(r'-?\d+', line)
        robots.append(Robot(int(x), int(y), int(dx), int(dy)))

def show(steps):
    grid = [ ['.'] * Width for _ in range(Height + 1) ]

    for robot in robots:
        x = (robot.x + steps * robot.dx) % Width
        y = (robot.y + steps * robot.dy) % Height
        grid[y][x] = '*'

    for row in grid:
        print(''.join(row))

i = 82
while True:
    print(i)
    show(i)
    time.sleep(0.1)
    i += 101
