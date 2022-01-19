#!/usr/bin/env python3

import sys
vertices = sys.stdin.readline().strip()
lines = sys.stdin.readlines()

def append(islands, k, v):
    v.append(k)
    islands.append(v)
    return islands

def CheckIfPath(k, v):
    return k in maps[v]

def addEdge(val1, val2):
    val1 = int(val1)
    val2 = int(val2)
    maps[val1].append(val2)
    maps[val2].append(val1)

maps = {}
for i in range(0, int(vertices)):
    maps[i] = []

for line in lines:
    line = line.strip()
    val1, val2 = line.split()
    addEdge(val1, val2)

islands = []
for k, v in maps.items():
    # print("-------------------", k , v)
    HasPath = False
    for i in islands:
        for j in i:
            if CheckIfPath(k, j):
                HasPath = True
                # print(j, True)
                break
    if not HasPath:
        islands = append(islands, k, v)
        # print("APPEND PLEASE")
    if len(islands) == 0:
        islands = append(islands, k, v)
        # print("APPEND PLEASE")

# print(f'Islands {len(islands)} -> {islands}')
print(len(islands))
