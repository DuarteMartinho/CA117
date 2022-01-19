#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    nums = line.rstrip().lower().split()
    num1 = nums[0]
    num2 = int(nums[1])
    if num2 != 10:
        num1 = num1[::-1]
        i = 0
        total = 0
        while i < len(num1):
            num = int(num1[i])
            total += (num * (num2 ** i))
            i += 1
        print(total)
    else:
        print(num1)
