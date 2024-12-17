#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    program = [ int(t) for t in f.readline().split(':')[1].split(',') ]

def run(a):
    b = 0
    c = 0
    ip = 0
    out = []

    while ip < len(program):
        instruction = program[ip]
        literal = program[ip + 1]
        combo = a if literal == 4 else b if literal == 5 else c if literal == 6 else literal
        ip += 2

        if instruction == 0: # ADV
            a = a // 2 ** combo
        elif instruction == 1: # BXL
            b = b ^ literal
        elif instruction == 2: # BST
            b = combo % 8
        elif instruction == 3: # JNZ
            if a != 0:
                ip = literal
        elif instruction == 4: # BXC
            b = b ^ c
        elif instruction == 5: # OUT
            out.append(combo % 8)
        elif instruction == 6: # BDV
            b = a // 2 ** combo
        elif instruction == 7: # CDV
            c = a // 2 ** combo

    return out

def find(a, j):
    if j < 0:
        return

    for i in range(8):
        newa = a | i << (3 * j)
        if run(newa)[j:] == program[j:]:
            if j == 0:
                print(newa, run(newa))
            else:
                find(newa, j - 1)

find(0, len(program) - 1)
