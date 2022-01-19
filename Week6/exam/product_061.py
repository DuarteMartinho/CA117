#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def getProduct(digits):
    total = 1
    for i in digits:
        total *= i
    return total

def main(num):
    finished = False
    while not finished:
        calc = []
        for c in str(num):
            if c != "0":
                calc.append(int(c))
        num = getProduct(calc)
        if num > 0 and num < 10:
            finished = True
        else:
            finished = False
    print(num)

for line in lines:
    line = line.strip()
    main(int(line))
