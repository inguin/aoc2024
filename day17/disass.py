#! /usr/bin/python

import sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"

with open(filename) as f:
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    program = [ int(t) for t in f.readline().split(':')[1].split(',') ]

ip = 0

while ip < len(program):
    instruction = program[ip]
    literal = program[ip + 1]
    combo = 'A' if literal == 4 else 'B' if literal == 5 else 'C' if literal == 6 else None

    if instruction == 0: # ADV
        opcode = "ADV"
        if combo:
            operation = f"A = A // {combo}"
        else:
            operation = f"A = A // {2**literal}"
    elif instruction == 1: # BXL
        opcode = "BXL"
        operation = f"B = B ^ {literal}"
    elif instruction == 2: # BST
        opcode = "BST"
        if combo:
            operation = f"B = {combo} % 8"
        else:
            operation = f"B = {literal % 8}"
    elif instruction == 3: # JNZ
        opcode = "JNZ"
        operation = f"if A: ip = {literal}"
    elif instruction == 4: # BXC
        opcode = "BXC"
        operation = "B = B ^ C"
    elif instruction == 5: # OUT
        opcode = "OUT"
        if combo:
            operation = f"print({combo} % 8)"
        else:
            operation = f"print({literal % 8})"
    elif instruction == 6: # BDV
        opcode = "BDV"
        if combo:
            operation = f"B = A // {combo}"
        else:
            operation = f"B = A // {2**literal}"
    elif instruction == 7: # CDV
        opcode = "CDV"
        if combo:
            operation = f"C = A // {combo}"
        else:
            operation = f"C = A // {2**literal}"

    print(f"{ip}: {instruction}, {literal} | {opcode} | {operation}")
    ip += 2
