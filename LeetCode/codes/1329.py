class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        if len(mat)==0:
            return []
        rows = len(mat)
        cols = len(mat[0])
        i, k, row = 0, 0, rows
        while i< rows*cols:
            r, c = row, k
            temp = []
            ids = []
            while r< rows and c<cols:
                temp.append(mat[r][c])
                ids.append((r,c))
                r+=1
                c+=1
                i+=1
                
            temp.sort()
            for x, y in ids:
                mat[x][y] = temp.pop(0)
            if row == 0:
                k+=1
                row = 0
            else:
                row-=1

        return mat