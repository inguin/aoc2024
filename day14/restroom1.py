#! /usr/bin/python

import re, sys
from collections import namedtuple

Width = 101
Height = 103
Seconds = 100

Robot = namedtuple('Robot', ('x', 'y', 'dx', 'dy'))
robots = []

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    for line in f:
        x, y, dx, dy = re.findall(r'-?\d+', line)
        robots.append(Robot(int(x), int(y), int(dx), int(dy)))

quadrants = [0, 0, 0, 0]

for robot in robots:
    x = (robot.x + Seconds * robot.dx) % Width
    y = (robot.y + Seconds * robot.dy) % Height
    if x < Width // 2 and y < Height // 2: quadrants[0] += 1
    if x < Width // 2 and y > Height // 2: quadrants[1] += 1
    if x > Width // 2 and y < Height // 2: quadrants[2] += 1
    if x > Width // 2 and y > Height // 2: quadrants[3] += 1
    print(x, y)

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])
