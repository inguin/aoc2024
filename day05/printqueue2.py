#! /usr/bin/python

import sys

def read_rules(f):
    rules = {}
    for line in f:
        if not line.strip():
            return rules
        a, b = [ int(x) for x in line.split('|') ]
        if b not in rules:
            rules[b] = set()
        rules[b].add(a)

def order_update(rules, update):
    pages = update.copy()
    ordered_pages = []

    while pages:
        for page in pages:
            others = set(p for p in pages if p != page)
            if not (page in rules and rules[page] & others):
                ordered_pages.append(page)
                pages.remove(page)
                break

    return ordered_pages

filename = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
with open(filename) as f:
    rules = read_rules(f)

    result = 0

    for line in f:
        update = [ int(n) for n in line.split(',') ]
        ordered = order_update(rules, update)
        if ordered != update:
            result += ordered[len(ordered) // 2]

    print(result)
