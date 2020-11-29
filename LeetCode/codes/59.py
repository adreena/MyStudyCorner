# time O(N2)
# space O(1) except for the output
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        output = [[None for i in range(n)] for j in range(n)]
        d = 0
        ci, cj =0, 0
        visited = set()
        for i in range(1, n*n+1):
            visited.add((ci,cj))
            output[ci][cj]=i
            ti, tj = ci+directions[d][0] , cj+directions[d][1]
            if 0<=ti<n and 0<=tj<n and (ti,tj) not in visited:
                ci = ti
                cj = tj
            else:
                d = (d+1)%4
                ci, cj = ci+directions[d][0] , cj+directions[d][1]
            
        return output