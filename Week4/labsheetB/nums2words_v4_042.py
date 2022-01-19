#!/usr/bin/env python3

import sys
availableNums = list(range(0, 101))
numsEng010 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
numsEng1119 = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
numsEngTies = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
lines = sys.stdin.readlines()

def main(line):
    i = 0
    while i < len(line):
        num = line[i]
        if int(num) in availableNums:
            numInt = int(num)
            if 0 <= numInt and numInt <= 10:
                pos = numInt
                out = numsEng010[pos]
                #print(out, numInt)
            elif 11 <= numInt and numInt <= 19:
                pos = numInt - 11
                out = numsEng1119[pos]
                #print(out, numInt)
            elif 20 <= numInt and numInt <= 99:
                decimal = numInt // 10 - 2
                units = numInt % 10
                if units == 0:
                    out = numsEngTies[decimal]
                else:
                    out = numsEngTies[decimal] + "-" + numsEng010[units]
                #print(out, numInt)
            elif numInt == 100:
                out = "one hundred"
            line[i] = out
        else:
            line[i] = num.replace(num, "unknown", 1)
        i += 1
    print(" ".join(line))

for line in lines:
    line = line.strip().split()
    main(line)
