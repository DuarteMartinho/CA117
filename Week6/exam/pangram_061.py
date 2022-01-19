#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def checkPangram(line):
    line = line.lower()
    a_to_z = "abcdefghijklmnopqrstuvwxyz"
    OutAZ = a_to_z
    for c in a_to_z:
        if line.count(c) >= 1:
            OutAZ = OutAZ.replace(c, "", 1)
    return OutAZ

for line in lines:
    line = line.strip()
    pangram = checkPangram(line)
    if len(pangram) == 0:
        print(f'pangram')
    else:
        print(f'missing {pangram}')
