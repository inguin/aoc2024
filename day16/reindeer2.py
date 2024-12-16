#! /usr/bin/python

import sys
from collections import defaultdict

North = (0, -1)
East = (1, 0)
South = (0, 1)
West = (-1, 0)
Left = { North: West, East: North, South: East, West: South }
Right = { North: East, East: South, South: West, West: North }

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = []

with open(filename) as f:
    for y, line in enumerate(f):
        line = line.strip()
        if 'S' in line:
            start = (line.index('S'), y)
            line = line.replace('S', '.')
        if 'E' in line:
            end = (line.index('E'), y)
            line = line.replace('E', '.')
        grid.append(line)

height = len(grid)
width = len(grid[0])

unvisited = {}
for y in range(height):
    for x in range(width):
        if grid[y][x] == '.':
            for heading in (North, East, South, West):
                unvisited[((x, y), heading)] = (99999999, None)
unvisited[(start, East)] = (0, {start})

unvisited_by_cost = defaultdict(list)
for node, (cost, path) in unvisited.items():
    unvisited_by_cost[cost].append(node)

def visit_node(node, cost, path):
    if node in unvisited:
        node_cost, node_path = unvisited[node]
        if cost < node_cost:
            unvisited_by_cost[node_cost].remove(node)
            if not unvisited_by_cost[node_cost]:
                del unvisited_by_cost[node_cost]

            unvisited[node] = (cost, path)
            unvisited_by_cost[cost].append(node)
        elif cost == node_cost:
            for p in path:
                unvisited[node][1].add(p)

while unvisited:
    print(len(unvisited))
    min_cost = min(unvisited_by_cost.keys())
    nearest_node = unvisited_by_cost[min_cost].pop()
    if not unvisited_by_cost[min_cost]:
        del unvisited_by_cost[min_cost]

    nearest_path = unvisited[nearest_node][1]
    del unvisited[nearest_node]

    pos, heading = nearest_node
    if pos == end:
        print(min_cost)
        print(len(nearest_path))
        break

    visit_node((pos, Left[heading]), min_cost + 1000, nearest_path)
    visit_node((pos, Right[heading]), min_cost + 1000, nearest_path)

    forward = (pos[0] + heading[0], pos[1] + heading[1])
    if grid[forward[1]][forward[0]] == '.':
        visit_node((forward, heading), min_cost + 1, nearest_path | {forward})
