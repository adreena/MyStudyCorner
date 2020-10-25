# time O(V+E)
# space O(V+E)
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(lambda:[])
        
        for a, b in tickets:
            heapq.heappush(graph[a], b)
            
        def DFS(loc, graph, path):
            while graph[loc]:
                nxt = heapq.heappop(graph[loc])
                DFS(nxt, graph, path)
            path.append(loc)
        
        path = ['JFK']
        DFS('JFK', graph, path)
        return path[::-1][:-1]