#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()
letters = ["A", "B", "C", "D"]

def main(line):
    numbers = []
    tokens = line.split()
    for c in tokens:
        numbers.append(int(c))
    numbers = sorted(numbers, reverse=True)
    return numbers

def printorder(listNums, order):
    answer = []
    for letterOrder in order:
        i = 0
        for c in letters:
            if c == letterOrder:
                answer.append(str(listNums[i]))
                break
            i += 1
    return " ".join(answer)

nums = lines[0].strip()
order = lines[1].strip()
numbers = main(nums)
res = printorder(numbers, order)
print(res)
