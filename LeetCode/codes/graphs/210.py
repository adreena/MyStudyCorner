# time O(NM)
# space: O(NM)

from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda:set())
        depths=defaultdict(lambda:0)

        for x,y in prerequisites:
            graph[y].add(x)
            depths[x]+=1
        
        q = []
        for i in range(numCourses):
            if i not in depths:
                q.append(i)
        path = []
        while q:
            top = q.pop(0)
            path.append(top)
            for nxt in graph[top]:
                depths[nxt]-=1
                if depths[nxt]==0:
                    q.append(nxt)
        if len(path)!=numCourses:
            return []
        return path