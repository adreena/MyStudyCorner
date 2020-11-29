# time: O(NM)
# space O(NM)
# 2 versions: DFS BFS

#BFS
class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        if len(grid)==0:
            return 0
        n, m= len(grid), len(grid[0])
        walls = 0
        def BFS(i, j):
            q= [(i,j)]
            # p = defaultdic(lambda:)
            while q:
                ci, cj = q.pop(0)
                visited.add((ci,cj))
                islands[-1].add((ci,cj))
                for ni,nj in [(ci+1,cj),(ci,cj+1),(ci-1,cj),(ci,cj-1)]:
                    if 0<=ni<n and 0<=nj<m:
                        if (ni,nj) not in visited and grid[ni][nj]==1 :
                            q.append((ni,nj))
                            visited.add((ni,nj))
                        elif grid[ni][nj]==0: # and (ni,nj) not in bound[-1]:
                            bound[-1].add((ni,nj))
                            perimeter[-1]+=1
        
        while True:
            islands= []
            perimeter = []
            bound = []
            visited = set()
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==1 and (i,j) not in visited:
                        islands.append(set())
                        bound.append(set())
                        perimeter.append(0)
                        BFS(i,j)
            if not islands:
                return walls
            # print(islands)
            # print('*',bound)
            # print(perimeter)
            max_id = bound.index(max(bound, key=len))
            walls+= perimeter[max_id]
            # print('>>', max_id, walls)
            # mark the region
            for i,island in enumerate(islands):
                if i== max_id: # add walls
                    for bi,bj in island:
                        grid[bi][bj] = 2
                else:
                    for bi,bj in bound[i]:
                        grid[bi][bj] = 1
            # for r in grid:
            #     print(r)
            # print('------------')
        return walls
            
#### DFS
class Solution:
    def containVirus(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        walls = 0
        def DFS(ci,cj):
            if (ci,cj) not in visited:
                visited.add((ci,cj))
                regions[-1].add((ci,cj))
                for ni,nj in [(ci+1,cj), (ci-1,cj), (ci,cj+1),(ci,cj-1)]:
                    if 0<=ni<n and 0<=nj<m:
                        if grid[ni][nj] == 1:
                            DFS(ni,nj)
                        elif grid[ni][nj]==0:
                            borders[-1].add((ni,nj))
                            perimeters[-1]+=1
                            
        
        while True:
            borders = []
            visited = set()
            perimeters = []
            regions = []
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==1 and (i,j) not in visited:
                        perimeters.append(0)
                        regions.append(set())
                        borders.append(set())
                        DFS(i,j)
            if not regions:
                break
            
            # find max border
            idx = borders.index(max(borders, key=len))
            walls+=perimeters[idx]
            
            for i, region in enumerate(regions):
                if i == idx:
                    # block region
                    for ci, cj in region:
                        grid[ci][cj]=-1
                else:
                    for ci, cj in region:
                        for ni, nj in [(ci+1,cj), (ci,cj+1),(ci,cj-1),(ci-1,cj)]:
                            if 0<=ni<n and 0<=nj<m and grid[ni][nj]==0:
                                grid[ni][nj]=1
        return walls