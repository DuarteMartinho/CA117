#!/usr/bin/env python3

def swap_unique_keys_values(d):
    newD = {}
    for k, v in d.items():
        if v not in newD:
            newD[v] = k, 1
        else:
            newD[v] = k, newD[v][1] + 1
    out = {}
    # print(newD)
    for k, v in newD.items():
        if newD[k][1] == 1:
            out[k] = newD[k][0]
    # print(out)
    return out
