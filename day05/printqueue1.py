#! /usr/bin/python

import sys

def read_rules(f):
    rules = {}
    for line in f:
        if not line.strip():
            return rules
        a, b = [ int(x) for x in line.split('|') ]
        if a not in rules:
            rules[a] = set()
        rules[a].add(b)

def check_update(rules, update):
    printed = set()
    for page in update:
        if page in rules and (rules[page] & printed):
            return False
        printed.add(page)
    return True

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(filename) as f:
    rules = read_rules(f)

    result = 0

    for line in f:
        update = [ int(n) for n in line.split(',') ]
        if check_update(rules, update):
            result += update[len(update) // 2]

    print(result)
