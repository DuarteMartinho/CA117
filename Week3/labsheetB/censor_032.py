#!/usr/bin/env python3

import sys
words = sys.stdin.readlines()
args = sys.argv[1]

with open(args, "r") as f_in:
    inputs = f_in.readlines()

for line in words:
    line = line.strip().split()
    i = 0
    while i < len(line):
        word = line[i]
        for censor in inputs:
            censor = censor.rstrip()
            if censor in word:
                line[i] = word.replace(censor, "@" * len(censor))
        i += 1
    print(" ".join(line))
