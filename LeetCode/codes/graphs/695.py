class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        islands = []
        n,m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    islands.append(1)
                    q = [(i,j)]
                    grid[i][j]=0
                    while q:
                        ci,cj = q.pop(0)
                        for ni, nj in [(ci+1,cj),(ci,cj+1),(ci,cj-1),(ci-1,cj)]:
                            if 0<=ni<n and 0<=nj<m and grid[ni][nj]==1:
                                grid[ni][nj]=0
                                islands[-1]+=1
                                q.append((ni,nj))
        if not islands:
            return 0
        return max(islands)