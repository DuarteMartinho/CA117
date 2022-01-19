#!/usr/bin/env python3

def swap_keys_values(d):
    newD = {}
    for k, v in d.items():
        newD[v] = k
    return newD
