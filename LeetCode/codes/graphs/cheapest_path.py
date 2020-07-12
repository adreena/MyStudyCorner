# dijkstra implentation is like BFS with a heap
# time: O(E+VlogV)
# space O(V)
import heapq
from collections import defaultdict

def dijkstra(x, y, graph):
    q = [(0, x)]
    visited = set()
    dists = defaultdict(lambda:float('inf'))
    dists[x] = 0
    while len(q)>0:
        price, node = heapq.heappop(q)
        visited.add(node)
        for nxt_node, nxt_price in graph[node]:
            dist[nxt_node] = min(dist[nxt_node], price+next_price)
            if nxt_node not in visited:
                heapq.heappush(q, (price+next_price, nxt_node))
                
    #checking if all nodes are accessible
    if len(dists)!=N:
        return -1
    return dists