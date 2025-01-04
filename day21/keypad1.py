#! /usr/bin/python

import sys

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
        if dcol > 0:
            sequence += '>' * dcol
        if drow < 0:
            sequence += '^' * (-drow)
        if dcol < 0 and pos[0] == 3 and keypos[1] == 0:
            sequence += '<' * (-dcol)
        if drow > 0 and pos[1] == 0 and keypos[0] == 3:
            sequence += 'v' * drow
        sequence += 'A'
        pos = keypos

    return sequence

def directional_keypad(code):
    positions = {}
    for row, keys in enumerate((' ^A', '<v>')):
        for col, key in enumerate(keys):
            positions[key] = (row, col)

    sequence = ''
    pos = positions['A']

    for key in code:
        keypos = positions[key]
        drow = keypos[0] - pos[0]
        dcol = keypos[1] - pos[1]
        if dcol < 0 and (pos[0] != 0 or keypos[1] != 0):
            sequence += '<' * (-dcol)
        if drow > 0:
            sequence += 'v' * drow
        if dcol > 0:
            sequence += '>' * dcol
        if drow < 0:
            sequence += '^' * (-drow)
        if dcol < 0 and pos[0] == 0 and keypos[1] == 0:
            sequence += '<' * (-dcol)
        sequence += 'A'
        pos = keypos

    return sequence

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

total = 0
with open(filename) as f:
    for line in f:
        code = line.strip()
        seq1 = numeric_keypad(code)
        seq2 = directional_keypad(seq1)
        seq3 = directional_keypad(seq2)
        result = int(code.strip('A')) * len(seq3)
        total += result
print(total)
