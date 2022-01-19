#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def findmedian(listNums):
    meanTotal = 0
    for c in listNums:
        meanTotal += c
    meanTotal = meanTotal / len(listNums)
    if len(listNums) % 2 == 0:
        mid1 = (len(listNums) // 2) - 1
        mid2 = (len(listNums) // 2)
        medianTotal = (listNums[mid1] + listNums[mid2]) / 2
    else:
        mid = len(listNums) // 2
        medianTotal = listNums[mid]
    print(f'Mean: {meanTotal:.1f}')
    print(f'Median: {medianTotal:.1f}')

nums = []
for line in lines:
    line = line.strip()
    nums.append(int(line))
findmedian(sorted(nums))
