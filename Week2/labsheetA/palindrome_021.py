#!/usr/bin/env python3

import sys
from string import punctuation
lines = sys.stdin.readlines()

def palindrome(left, right):
    for c in left:
        if c in right:
            right = right.replace(c, "", 1)
        else:
            return False
    return right == ""

for line in lines:
    line = line.rstrip()
    for i in line:
        if i in punctuation or i == " ":
            line = line.replace(i, "", 1)
        line = line.lower()

    if len(line) % 2 == 1:
        mid = len(line) // 2
        left = line[:mid]
        right = line[mid + 1:]
    else:
        mid = len(line) // 2
        left = line[:mid]
        right = line[mid:]
    res = palindrome(left, right)
    print(res)
