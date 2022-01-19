#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
d = {}
skipped = []

def main(name, marks):
    marks = marks.split(',')
    total = 0
    for m in marks:
        try:
            total += int(m)
        except ValueError:
            skipped.append(name)
            break
    d[name] = total

def printout():
    for k, v in sorted(d.items(), reverse=True, key=lambda item: item[1]):
        if k not in skipped:
            print(f'{k} : {v}')
    print(f'Skipped:')
    for n in skipped:
        print(f'{n}')

for line in lines:
    line = line.strip()
    name, marks = line.split(":")
    main(name, marks)
printout()
