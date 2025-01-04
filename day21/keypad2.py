#! /usr/bin/python

import sys
from functools import lru_cache

def numeric_keypad(code):
    positions = {}
    for row, keys in enumerate(('789', '456', '123', ' 0A')):
        for col, key in enumerate(keys):
            positions[key] = (row, col)

    sequence = ''
    pos = positions['A']

    for key in code:
        keypos = positions[key]
        drow = keypos[0] - pos[0]
        dcol = keypos[1] - pos[1]
        if dcol < 0 and (pos[0] != 3 or keypos[1] != 0):
            sequence += '<' * (-dcol)
        if drow > 0 and (pos[1] != 0 or keypos[0] != 3):
            sequence += 'v' * drow
        if drow < 0:
            sequence += '^' * (-drow)
        if dcol > 0:
            sequence += '>' * dcol
        if dcol < 0 and pos[0] == 3 and keypos[1] == 0:
            sequence += '<' * (-dcol)
        if drow > 0 and pos[1] == 0 and keypos[0] == 3:
            sequence += 'v' * drow
        sequence += 'A'
        pos = keypos

    return sequence

@lru_cache(maxsize=None)
def directional_keypad(code, level):
    positions = {}
    for row, keys in enumerate((' ^A', '<v>')):
        for col, key in enumerate(keys):
            positions[key] = (row, col)

    result = 0
    pos = positions['A']

    for key in code:
        sequence = ''
        keypos = positions[key]
        drow = keypos[0] - pos[0]
        dcol = keypos[1] - pos[1]
        if dcol < 0 and (pos[0] != 0 or keypos[1] != 0):
            sequence += '<' * (-dcol)
        if drow > 0:
            sequence += 'v' * drow
        if drow < 0 and (pos[1] != 0 or keypos[0] != 0):
            sequence += '^' * (-drow)
        if dcol > 0:
            sequence += '>' * dcol
        if dcol < 0 and pos[0] == 0 and keypos[1] == 0:
            sequence += '<' * (-dcol)
        if drow < 0 and pos[1] == 0 and keypos[0] == 0:
            sequence += '^' * (-drow)
        sequence += 'A'
        pos = keypos
        if level > 1:
            result += directional_keypad(sequence, level - 1)
        else:
            result += len(sequence)

    return result

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0
with open(filename) as f:
    for line in f:
        code = line.strip()
        seq = numeric_keypad(code)
        result = int(code.strip('A')) * directional_keypad(seq, 25)
        total += result
print(total)
# x < 272795278188520
# x != 188122209881868
