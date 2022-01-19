#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def getSimplicity(word):
    letters = []
    for c in word:
        if c not in letters:
            letters.append(c)
    if len(letters) > 2:
        Simplicity = len(letters) - 2
    else:
        Simplicity = 0
    print(f'{Simplicity}')

for line in lines:
    line = line.strip()
    getSimplicity(line)
