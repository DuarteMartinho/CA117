#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def wordinvert(word):
    chars = []
    chars2 = []
    k = 0
    for c in word:
        k += 1
        if k % 2 != 0:
            chars.append(c)
        else:
            chars2.append(c)
    # print(chars, chars2)
    i = 0
    j = 0
    while i < len(chars) and j < len(chars2):
        tmp = chars[i]
        chars[i] = chars2[j]
        chars2[j] = tmp
        i += 1
        j += 1
    # print(chars, chars2)
    final = []
    z = 0
    while z < len(chars):
        final.append(chars[z])
        try:
            final.append(chars2[z])
        except IndexError:
            break
        z += 1
    return final

for line in lines:
    line = line.rstrip()
    res = wordinvert(line)
    print("".join(res))
