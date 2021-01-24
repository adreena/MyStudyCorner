class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix)==0:
            return []
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        r, c = 0,0
        output = []
        directions = [[-1,1],[1,-1]]
        i, d = 0, 0
        while i < rows*cols:
            output.append(matrix[r][c])
            nr = r+directions[d][0]
            nc = c+directions[d][1]
            if 0<=nr<rows and 0<=nc<cols:
                r , c = nr, nc
            else:
                d = (d+1)%2
                if nr<0:
                    c+=1
                    if c==cols:
                        c = cols-1
                        r = r+1
                else:
                    r+=1
                    if r==rows:
                        r = rows-1
                        c+=1
            i+=1
        return output
                