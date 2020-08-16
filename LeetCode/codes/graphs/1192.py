
# time O(V+E)
# space: O(V+E)

from collections import defaultdict
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def DFS(node):
            self.low[node]=self.time
            self.disc[node] = self.time
            self.time +=1
            self.visited[node] = True
            for nxt in self.graph[node]:
                if not self.visited[nxt]:
                    self.parent[nxt] = node
                    DFS(nxt)
                    self.low[node]=min(self.low[nxt], self.low[node])
                    if self.low[nxt]>self.disc[node]:
                        self.critical.add(tuple(sorted([node, nxt])))
                elif self.parent[node]!=nxt:
                    self.low[node] = min(self.low[node], self.disc[nxt])
        self.time = 0
        self.low = defaultdict(lambda:0)
        self.disc = defaultdict(lambda:0)
        self.visited = defaultdict(lambda:False)
        self.parent=defaultdict(lambda:None)
        self.graph = defaultdict(lambda:[])
        self.critical = set()
        for a,b in connections:
            self.graph[a].append(b)
            self.graph[b].append(a)
        
        for i in range(n):
            if not self.visited[i]:
                DFS(i)
        return self.critical