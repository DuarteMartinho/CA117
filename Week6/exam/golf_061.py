#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
d = {}
invalid = []

def getName(line):
    line = line[::-1].split()
    nameBackward = " ".join(line[3:])
    name = nameBackward[::-1]
    scores = line[:3]
    return (name, scores)

def getScores(name, scores):
    newScores = 0
    try:
        for s in scores:
            newScores += int(s)
        return newScores
    except ValueError:
        invalid.append(name)
        return 0

def createDisctionary(name, score):
    d[name] = score

for line in lines:
    line = line.strip()
    name, scores = getName(line)
    newScores = getScores(name, scores)
    createDisctionary(name, newScores)

for k, v in sorted(d.items(), key=lambda item: item[1]):
    if v != 0:
        print(f'{k}: {v}')

if len(invalid) >= 1:
    invalid = ", ".join(invalid)
    print(f'Disqualified: {invalid}')
