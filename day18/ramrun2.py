#! /usr/bin/python

import sys
from collections import defaultdict

Width = 71
Height = 71
Goal = (Width - 1, Height - 1)

North = (0, -1)
East = (1, 0)
South = (0, 1)
West = (-1, 0)

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
grid = [ (['.'] * Width) for _ in range(Height) ]

def exit_blocked():
    unvisited = {}
    for y in range(Height):
        for x in range(Width):
            if grid[y][x] == '.':
                unvisited[(x, y)] = 99999999
    unvisited[(0, 0)] = 0

    unvisited_by_cost = defaultdict(list)
    for node, cost in unvisited.items():
        unvisited_by_cost[cost].append(node)

    def visit_node(node, cost):
        if node in unvisited:
            node_cost = unvisited[node]
            if cost < node_cost:
                unvisited_by_cost[node_cost].remove(node)
                if not unvisited_by_cost[node_cost]:
                    del unvisited_by_cost[node_cost]

                unvisited[node] = cost
                unvisited_by_cost[cost].append(node)

    while True:
        print(len(unvisited))
        min_cost = min(unvisited_by_cost.keys())
        if min_cost == 99999999:
            return True

        nearest_node = unvisited_by_cost[min_cost].pop()
        if not unvisited_by_cost[min_cost]:
            del unvisited_by_cost[min_cost]
        del unvisited[nearest_node]

        if nearest_node == Goal:
            return False

        x, y = nearest_node
        visit_node((x - 1, y), min_cost + 1)
        visit_node((x + 1, y), min_cost + 1)
        visit_node((x, y - 1), min_cost + 1)
        visit_node((x, y + 1), min_cost + 1)

with open(filename) as f:
    for line in f:
        x, y = (int(t) for t in line.split(','))
        grid[y][x] = '#'
        if exit_blocked():
            print(f"{x},{y}")
            break
