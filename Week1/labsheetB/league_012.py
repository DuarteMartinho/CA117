#!/usr/bin/env python3

import sys

lines = sys.stdin.readlines()
allLines = []

i = 0
while i < len(lines):
    tokens = lines[i].rstrip().split()
    j = 1
    while j < len(tokens):
        token = tokens[j]
        if token[0].isdigit():
            team_name = " ".join(tokens[1:j])
            j = j - 1
            while j != 1:
                tokens.pop(2)
                j -= 1
            break
        j += 1

    # print(tokens)
    tokens[0] = tokens[0]
    tokens[1] = team_name
    allLines.append(tokens)
    # print(allLines)
    i += 1

#print(allLines)
longest = 0
for lines in allLines:
    line = lines[1]
    #print(line)
    if len(line) > longest:
        longest = len(line)
#print(longest)

title = "POS CLUB" + ((longest - 4) * " ") + "  P   W   D   L  GF  GA  GD PTS"
print(title)

for line in allLines:
    spacesPos = (3 - len(line[0])) * " "
    spacesClub = (longest - len(line[1])) * " "
    spacesP = (2 - len(line[2])) * " "
    spacesW = (3 - len(line[3])) * " "
    spacesD = (3 - len(line[4])) * " "
    spacesL = (3 - len(line[5])) * " "
    spacesGF = (3 - len(line[6])) * " "
    spacesGA = (3 - len(line[7])) * " "
    spacesGD = (3 - len(line[8])) * " "
    spacesPTS = (3 - len(line[9])) * " "
    Pos = spacesPos + line[0]
    Club = " " + line[1] + spacesClub
    P = " " + spacesP + line[2]
    W = " " + spacesW + line[3]
    D = " " + spacesD + line[4]
    L = " " + spacesL + line[5]
    GF = " " + spacesGF + line[6]
    GA = " " + spacesGA + line[7]
    GD = " " + spacesGD + line[8]
    PTS = " " + spacesPTS + line[9]
    total = Pos + Club + P + W + D + L + GF + GA + GD + PTS
    print(total)
