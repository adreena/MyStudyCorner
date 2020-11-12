# time O(NM)
# space O(NM)
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if len(M)==0:
            return 0
        friends=0
        visited = set()
        for i in range(len(M)):
            if i not in visited:
                q=[i]
                friends+=1
                while q:
                    ci = q.pop(0)
                    for nj in range(len(M)):
                        if nj not in visited and M[ci][nj]==1:
                            q.append(nj)
                            visited.add(nj)
        return friends