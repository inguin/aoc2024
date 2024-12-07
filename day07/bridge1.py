#! /usr/bin/python

import sys

def solvable(result, operands):
    if len(operands) == 1:
        return result == operands[0]
    return solvable(result - operands[-1], operands[:-1]) or \
           (result % operands[-1] == 0 and solvable(result // operands[-1], operands[:-1]))

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0

with open(filename) as f:
    for line in f:
        result, operands = line.split(':')
        result = int(result)
        operands = [int(operand) for operand in operands.split()]
        if solvable(result, operands):
            total += result

print(total)
