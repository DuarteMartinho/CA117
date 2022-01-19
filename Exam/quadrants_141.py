#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def main(x, y):
    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(2)
    elif x < 0 and y < 0:
        print(3)
    elif x < 0 and y > 0:
        print(4)

for line in lines:
    line = line.strip()
    x, y = line.split()
    main(int(x), int(y))
