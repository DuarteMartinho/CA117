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

    def hasPathTo(self, v):
        return (self.s in self.g.adj[v])

    def pathTo(self, v, hops):
        for i in range(hops + 1):
            print("dadas", i)
        pathTo = [v]
        x = v
        while x != 0:
            x = self.parent[x]
            pathTo.append(x)
        pathTo.reverse()
        return pathTo
