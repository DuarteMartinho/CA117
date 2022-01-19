#!/usr/bin/env python3

import sys
lines = sys.stdin.readlines()

wins = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

def getResult(p1, p2):
    if wins[p1] == p2:
        return 1
    elif wins[p2] == p1:
        return 2
    else:
        return 0

for line in lines:
    line = line.strip()
    P1, P2 = line.split()
    # print(f'{P1} vs {P2}')
    res = getResult(P1, P2)
    if res > 0:
        print(f'Player {res} wins')
    else:
        print(f'Draw')
