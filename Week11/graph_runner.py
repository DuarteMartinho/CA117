import sys

from graph_111 import Graph, DFSPaths

def main():

    with open('graph01.txt') as f:

        V = int(f.readline())

        g = Graph(V)

        for line in f:

            v, w = [int(t) for t in line.strip().split()]
            g.addEdge(v, w)

    paths = DFSPaths(g, 0)

    print(paths.hasPathTo(6))
    print(paths.pathTo(6))

if __name__ == '__main__':
    main()