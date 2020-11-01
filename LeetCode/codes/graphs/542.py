# tim eO(NM)
# space O(NM)
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if len(matrix)==0:
            return []
        m,n = len(matrix[0]), len(matrix)
        q=[]
        visited = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    visited.add((i,j))
                    q.append((i,j))
        
        
        while q:
            while q:
                ci, cj = q.pop(0)
                for ni, nj in [(ci+1,cj),(ci-1,cj),(ci,cj-1),(ci,cj+1)]:
                    if 0<=ni<n and 0<=nj<m and (ni,nj) not in visited:
                            matrix[ni][nj] = matrix[ci][cj]+1
                            q.append((ni,nj))
                            visited.add((ni,nj))
                
        return matrix
                                