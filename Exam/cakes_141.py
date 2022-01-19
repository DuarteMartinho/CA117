#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def main(allvals):
    # print("---------------------------------")
    allvals = sorted(allvals)[::-1]
    # print(allvals)
    i = 0
    j = 0
    total = 0
    realtotal = 0
    last3 = []
    while i < len(allvals):
        val = int(allvals[i])
        # print(i, val, j)
        if j == 2:
            last3.append(val)
            # print("RESET", last3)
            last3.pop()
            # print("RESET2", last3)
            for k in last3:
                realtotal += k
            total = 0
            j = 0
            last3 = []
        else:
            total += val
            last3.append(val)
            j += 1
        i += 1
    # print("REAL TOTAL",  realtotal)
    # print("OTHER TOTAL",  total)
    print(realtotal + total)

for line in lines:
    line = line.strip()
    tokens = line.split()
    main(tokens)
