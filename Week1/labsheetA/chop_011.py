#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for word in lines:
    word = word.rstrip()[1:-1]
    if len(word) > 0:
        print(word)
