# time O(NM)
# space O(NM)

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        q = []
        cost = 0
        n,m = len(grid), len(grid[0])
        dp = [[float('inf') for i in range(m)] for j in range(n)]
        def DFS(i,j):
            # find a reachable
            if 0<=i<n and 0<=j<m and dp[i][j]==float('inf'):
                dp[i][j]=cost
                q.append((i,j))
                ni = i+direction[grid[i][j]-1][0]
                nj = j+direction[grid[i][j]-1][1]
                DFS(ni,nj)
        
        DFS(0,0)
        while q:
            q, q_copy = [], q
            cost+=1
            for ci, cj in q_copy:
                for x,y in direction:
                    DFS(ci+x, cj+y)
        
        return dp[-1][-1]