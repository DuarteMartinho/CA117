#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

def OrderABC(nums, abc):
    # print(nums)
    i = 0
    while i < len(nums):
        j = i + 1
        while j < len(nums):
            if int(nums[i]) > int(nums[j]):
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
            j = j + 1
        i += 1
    A = nums[0]
    B = nums[1]
    C = nums[2]
    # print(nums)
    # print(abc)
    answer = []
    for c in abc:
        if c == "A":
            answer.append(A)
        elif c == "B":
            answer.append(B)
        elif c == "C":
            answer.append(C)
    answerLine = " ".join(answer)
    return answerLine

abcNums = lines[0].split()
abcOrder = lines[1]
res = OrderABC(abcNums, abcOrder)
print(res)
