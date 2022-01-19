#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    password = line.rstrip()
    security = [0, 0, 0, 0]
    for char in password:
        if char.isdigit():
            security[0] = 1
        elif char.islower():
            security[1] = 1
        elif char.isupper():
            security[2] = 1
        else:
            security[3] = 1
    print(sum(security))
