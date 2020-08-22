
# time :(O(NM)
# space O(NM)

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        islands = defaultdict(lambda:[])
        shapes = set()
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                shape = set()
                if grid[i][j] == 1:
                    q = [(i,j,i,j)]
                    shape.add((0,0))
                    grid[i][j]=2
                    while q:
                        ci, cj, c0, r0 = q.pop(0)
                        shape.add((ci-c0, cj-r0))
                        for ni, nj in [(ci+1,cj), (ci-1,cj), (ci, cj+1), (ci, cj-1)]:
                            if 0<=ni<n  and 0<=nj<m and grid[ni][nj]==1:
                                q.append((ni,nj,c0,r0))
                                grid[ni][nj] = 2
                    # print(shape)
                    if shape:
                        shapes.add(frozenset(shape))
        # for r in grid:
        #     print(r)
        # print(shapes)
        return len(shapes)
        