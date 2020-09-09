# time O(E+V)
# space O(V+E)

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(lambda:set())
        visited = defaultdict(lambda:0)
        for a, b in prerequisites:
            graph[b].add(a)
        
        def dfs_cycle(course, graph, visited):
            if visited[course] == 1:
                return True
            if visited[course] == -1:
                return False
            visited[course] = 1
            for nxt in graph[course]:
                if dfs_cycle(nxt, graph,visited):
                    return True
            visited[course] = -1
            return False
        
        for i in range(numCourses):
            if dfs_cycle(i, graph, visited):
                return False
        return True