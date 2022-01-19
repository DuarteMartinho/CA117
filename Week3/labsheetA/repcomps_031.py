#!/usr/bin/env python3

import sys
numsIn = sys.stdin.readlines()
def main(num):
    nums = range(1, num + 1)
    a = ['X' if n % 3 == 0 else n for n in list(nums)]
    print("Multiples of 3 replaced: " + str(a))

for n in numsIn:
    n = n.rstrip()
    main(int(n))
