
#time O(NM)
#space O(NM)


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rottens = []
        if len(grid)==0:
            return 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rottens.append((i,j,0))
        
        max_d = 0
        while rottens:
            ci, cj, cd = rottens.pop(0)
            for ni, nj in [(ci+1, cj), (ci-1, cj), (ci, cj+1), (ci, cj-1)]:     
                if 0<=ni<n and 0<=nj<m and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    max_d = max(cd+1, max_d)
                    rottens.append((ni,nj,cd+1))
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return max_d