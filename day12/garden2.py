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

def get_plant(row, col):
    if row < 0 or row >= len(grid):
        return None
    if col < 0 or col >= len(grid[row]):
        return None
    return grid[row][col]

def has_top_fence(row, col):
    return get_plant(row, col) != get_plant(row - 1, col)

def has_bottom_fence(row, col):
    return get_plant(row, col) != get_plant(row + 1, col)

def has_left_fence(row, col):
    return get_plant(row, col) != get_plant(row, col - 1)

def has_right_fence(row, col):
    return get_plant(row, col) != get_plant(row, col + 1)

def count_sides(region):
    region = sorted(region)
    sides = 0
    for (row, col) in region:
        plant = get_plant(row, col)
        if has_top_fence(row, col):
            if get_plant(row, col - 1) != plant or not has_top_fence(row, col - 1):
                sides += 1
        if has_bottom_fence(row, col):
            if get_plant(row, col - 1) != plant or not has_bottom_fence(row, col - 1):
                sides += 1
        if has_left_fence(row, col):
            if get_plant(row - 1, col) != plant or not has_left_fence(row - 1, col):
                sides += 1
        if has_right_fence(row, col):
            if get_plant(row - 1, col) != plant or not has_right_fence(row - 1, col):
                sides += 1
    return sides

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
        print(sorted(region))

total = 0

for region in unique_regions:
    plant = grid[region[0][0]][region[0][1]]
    fields = len(region)
    sides = count_sides(region)
    print(plant, fields, sides)
    total += fields * sides

print(total)
