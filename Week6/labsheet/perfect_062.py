#!/usr/bin/env python3

import sys
import math
lines = sys.stdin.readlines()

def sumFac(n):
    total = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i
    return total - n

for line in lines:
    line = int(line.rstrip())
    total = sumFac(line)
    print(f'{line == total}')
