#!/usr/bin/env python3

def build_dictionary(stream):
    d = {}
    stream = stream.readlines()
    for line in stream:
        line = line.strip()
        animal, value = line.split()
        d[animal] = int(value)
    return d

def extract_range(d, low, high):
    nd = {}
    for k, v in d.items():
        if low <= v <= high:
            nd[k] = v
    return nd
