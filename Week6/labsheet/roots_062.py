#!/usr/bin/env python3

import sys
import math
lines = sys.stdin.readlines()

def calcRoots(a, b, c):
    try:
        sqRoot = math.sqrt((b ** 2) - (4 * a * c))
        r1 = ((-1 * b) + sqRoot) / (2 * a)
        r2 = ((-1 * b) - sqRoot) / (2 * a)
        print(f'r1 = {r1}, r2 = {r2}')
    except ValueError:
        print(f'None')

for line in lines:
    line = line.strip()
    a, b, c = line.split()
    calcRoots(int(a), int(b), int(c))
