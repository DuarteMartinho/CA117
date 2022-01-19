#!/usr/bin/env python3

from random import sample
import sys
numsIn = sys.stdin.readlines()

def main(num):
    nums = range(1, num + 1)
    #print(list(nums))
    mult3 = [n for n in list(nums) if n % 3 == 0]
    mult3sq = [n ** 2 for n in list(nums) if n % 3 == 0]
    mult4double = [n * 2 for n in list(nums) if n % 4 == 0]
    mult3or4 = [n for n in list(nums) if n % 3 == 0 or n % 4 == 0]
    mult3and4 = [n for n in list(nums) if n % 3 == 0 and n % 4 == 0]
    print("Multiples of 3: " + str(mult3))
    print("Multiples of 3 squared: " + str(mult3sq))
    print("Multiples of 4 doubled: " + str(mult4double))
    print("Multiples of 3 or 4: " + str(mult3or4))
    print("Multiples of 3 and 4: " + str(mult3and4))
    #print("-------------------------------------------------------------------")

for n in numsIn:
    n = n.rstrip()
    main(int(n))
