
# time :(O(NM)
# space O(NM)

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        shapes = set()
        
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    q = [(i,j)]
                    start = (i,j)
                    grid[i][j]=0
                    shape = {(0,0)}
                    while q:
                        ci, cj= q.pop(0)
                        shape.add((ci-start[0],cj-start[1]))
                        for ni, nj in [(ci+1,cj),(ci,cj+1),(ci-1,cj),(ci,cj-1)]:
                            if 0<=ni<n and 0<=nj<m and grid[ni][nj]==1:
                                grid[ni][nj]=0
                                q.append((ni,nj))
                    if shape:
                        shapes.add(frozenset(shape))
        return len(shapes)
        