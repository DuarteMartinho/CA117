#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def anagram(left, right):
    for c in left:
        if c in right:
            right = right.replace(c, "", 1)
        else:
            return False
    return right == ""

for line in lines:
    tokens = line.strip().split()
    left, right = tokens
    #print(tokens)
    #print(left)
    #print(right)
    res = anagram(left, right)
    print(res)
