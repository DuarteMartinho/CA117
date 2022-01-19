#!/usr/bin/env python3

lines = ['Jimmy', 'ran', 'to', 'a', 'standstill']
i = 0
while i < len(lines):
    word = lines[i][1:len(lines[i]) - 1]
    print(word)
    i += 1

for word in lines:
    print(word[1:len(word) - 1])
