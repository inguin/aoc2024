#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    grid = [ line.strip() for line in f ]

regions = {}

def merge_regions(region1, region2):
    if region1 is region2:
        return
    region1 += region2
    for row, col in region2:
        regions[(row, col)] = region1

def fence_cost(row, col):
    cost = 0
    plant = grid[row][col]
    if row == 0 or grid[row - 1][col] != plant:
        cost += 1
    if row + 1 == len(grid) or grid[row + 1][col] != plant:
        cost += 1
    if col == 0 or grid[row][col - 1] != plant:
        cost += 1
    if col + 1 == len(grid[row]) or grid[row][col + 1] != plant:
        cost += 1
    return cost

for row, line in enumerate(grid):
    for col, plant in enumerate(line):
        region = [(row, col)]
        if col > 0 and line[col - 1] == plant:
            merge_regions(region, regions[(row, col - 1)])
        if row > 0 and grid[row - 1][col] == plant:
            merge_regions(region, regions[(row - 1, col)])
        regions[(row, col)] = region

unique_regions = []
for region in regions.values():
    if region not in unique_regions:
        unique_regions.append(region)

total = 0

for region in unique_regions:
    plant = grid[region[0][0]][region[0][1]]
    fields = len(region)
    fence = sum(fence_cost(row, col) for (row, col) in region)
    print(plant, fields, fence)
    total += fields * fence

print(total)
