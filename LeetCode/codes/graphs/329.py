# time : O(MN) each cell will be calculated only once through DFS and DFS time is O(V+E) as for matrix it's the total number of cells M*N
# space: O(MN)
from collections import defaultdict
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    self.cache = defaultdict(lambda:0)
    max_path = 0

    def DFS(i, j, matrix):
        if (i,j) in self.cache:
            return self.cache[(i,j)]
        for ni, nj in [(i+1,j), (i-1,j), (i, j+1), (i,j-1)]:
            if 0<=ni<len(matrix) and 0<=nj<len(matrix[0]) and matrix[ni][nj]>matrix[i][j]:
                self.cache[(ni,nj)] = DFS(ni, nj, matrix)
                self.cache[(i,j)] = max(self.cache[(i,j)], self.cache[(ni,nj)])
        self.cache[(i,j)]+=1
        return self.cache[(i,j)]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            max_path = max(max_path, DFS(i, j, matrix))

    return max_path
