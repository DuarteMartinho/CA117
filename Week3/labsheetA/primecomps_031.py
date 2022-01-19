#!/usr/bin/env python3

import sys
numsIn = sys.stdin.readlines()

def main(numsIn):
    nums = list(range(1, numsIn + 1))
    primes = []
    for n in nums:
        if n > 1:
            numsRange = range(2, n)
            for i in numsRange:
                if n % i == 0:
                    break
            else:
                primes.append(n)
        print(n)
    print("Primes: " + str(primes))

for n in numsIn:
    n = n.rstrip()
    main(int(n))
