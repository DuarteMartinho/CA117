#!/usr/bin/env python3

import sys

total = 0
for line in sys.stdin.readlines():
    token = line.strip().split()
    total = total + len(token)
print(total)
