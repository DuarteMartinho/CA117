#!/usr/bin/env python3

import sys
import string

tokens = []
total = 0
for line in sys.stdin.readlines():
    token = line.strip().split()
    for i in token:
        i = i.lower()
        for c in i:
            if c in string.punctuation:
                i = i.replace(c, "", 1)
        if i not in tokens and len(i) > 0:
            i = i
            tokens.append(i)
print(len(tokens))
