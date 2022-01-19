#!/usr/bin/env python3

import sys

class Graph(object):

    def __init__(self, V):
        self.adj = {}
        self.V = V
        for v in range(V):
            self.adj[v] = list()

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

class DFSPaths(object):

    def __init__(self, g, s):
        self.g = g
        self.s = s
        self.visited = [False for _ in range(g.V)]
        self.parent = [False for _ in range(g.V)]
        self.dfs(s)

    def dfs(self, v):
        self.visited[v] = True
        for w in self.g.adj[v]:
            if not self.visited[w]:
                self.parent[w] = v
                self.dfs(w)

    def hops(self, v, hops):
        hopspath = [v]
        x = [v]
        for i in range(hops):
            for parent in x:
                for j in self.g.adj[parent]:
                    if j not in hopspath:
                        hopspath.append(j)
            x = (self.g.adj[parent])
            hops -= 1
        return sorted(hopspath)

args = sys.argv[2:]
with open(sys.argv[1], 'r') as f:
    vertices = int(f.readline())
    g = Graph(vertices)

    for line in f:
        v, w = [int(t) for t in line.strip().split()]
        g.addEdge(v, w)

    paths = DFSPaths(g, 0)
    print(paths.hops(int(args[0]), int(args[1])))
