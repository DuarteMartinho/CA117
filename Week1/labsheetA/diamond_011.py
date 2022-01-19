#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

for line in lines:
    num = int(line.rstrip())
    spaces = " "
    char = "* "
    amountLines = num * 2
    i = num
    while i != 0:
        print((i - 1) * spaces + char * (((num - i + 1)) - 1) + "*")
        i -= 1
    num = num - 1
    i = 0
    while num != 0:
        i += 1
        print((spaces * (i)) + (((num) - 1) * char) + "*")
        num -= 1
