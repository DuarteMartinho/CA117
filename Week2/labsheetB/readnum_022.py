#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    line = line.strip()
    try:
        num = int(line)
        print(f'Thank you for {num}')
        break
    except ValueError:
        print(f'{line} is not a number')
