#!/usr/bin/env python3

import math
import sys
lines = sys.stdin.readlines()

for line in lines:
    numplaces = line.rstrip()
    decplaces = int(numplaces)
    print(f'{math.pi:.{decplaces}f}')
