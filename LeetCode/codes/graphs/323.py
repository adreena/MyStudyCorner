# O(V+E)
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(lambda:[])
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        count = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                count+=1
                q = [i]
                while q:
                    top = q.pop(0)
                    for nxt in graph[top]:
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append(nxt)
        return count