# dijkstra 
# time O(E+VlgV)
# space O(V)

from collections import defaultdict
import heapq
def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
    graph = defaultdict(lambda:[])
    for edge, prob in zip(edges, succProb):
        graph[edge[0]].append([edge[1], prob])
        graph[edge[1]].append([edge[0], prob])

    q = [(-1., start)]
    visited = set()
    dist = defaultdict(lambda: float('-inf'))
    while len(q)>0:
        d, node = heapq.heappop(q)
        visited.add(node)
        for nxt, prob in graph[node]:
            dist[nxt] = max(-prob*d, dist[nxt])
            if nxt not in visited:
                heapq.heappush(q, (prob*d, nxt))
    if end not in dist:
        return 0.
    return dist[end]