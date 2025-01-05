#! /usr/bin/python

import re, sys

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
signals = {}

with open(filename) as f:
    for line in f:
        line = line.strip()
        if not line:
            break
        signal, level = line.split(": ")
        signals[signal] = bool(int(level))

    for line in f:
        line = line.strip()
        m = re.match(r"(\w+) (\w+) (\w+) -> (\w+)", line)
        op1, op, op2, signal = m.groups()
        signals[signal] = (op, op1, op2)

def calc(signal):
    s = signals[signal]
    if not isinstance(s, tuple):
        return s
    op, op1, op2 = s
    val1 = calc(op1)
    val2 = calc(op2)
    if op == 'AND': return val1 and val2
    if op == 'OR': return val1 or val2
    if op == 'XOR': return val1 ^ val2

result = 0

for signal in signals:
    if signal.startswith("z"):
        pos = int(signal[1:])
        result |= calc(signal) << pos

print(result)
