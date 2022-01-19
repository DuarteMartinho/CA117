#!/usr/bin/env python3

import sys
line = sys.stdin.read().strip().split()

def main():
    nRooms = line[0]
    occupied = line[1:]
    if int(nRooms) == len(occupied):
        print(f'no room')
    elif int(nRooms) > len(occupied):
        ordered = []
        for i in occupied:
            ordered.append(int(i))
        ordered = sorted(ordered)
        i = 1
        for j in ordered:
            if j > i:
                print(f'{i}')
                return
            i += 1
        print(i)
main()
