# time: O(MN)
# space: O(MN)


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = '0'
                    q = [(i,j)]
                    islands +=1
                    while q:
                        ci, cj = q.pop(0)
                        for ni, nj in [(ci+1,cj), (ci,cj+1), (ci-1,cj), (ci,cj-1)]:
                            if 0<=ni<len(grid) and 0<=nj<len(grid[0]) and grid[ni][nj]=='1':
                                grid[ni][nj] = '0'
                                q.append((ni,nj))
                    
        return islands