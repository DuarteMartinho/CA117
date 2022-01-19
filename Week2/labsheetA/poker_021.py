#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

hands = ["nothing", "one pair", "two pairs", "three of a kind", "a straight", "a flush", "a full house", "four of a kind", "a straight flush", "a royal flush"]
totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in lines:
    line = line.rstrip().split(",")
    position = int(line[10])
    totals[position] = totals[position] + 1

i = 0
totals[10] = len(lines)
total = totals[10]
while i < len(totals) - 1:
    percentage = (totals[i] / total) * 100
    handName = hands[i]
    print(f'The probability of {handName} is {percentage:.4f}%')
    i += 1
