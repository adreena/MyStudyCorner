# time O(MN)
# space O(1)
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        direction = [[0,1], [1,0], [0,-1],[-1,0]]
        cc, cr = 0, 0
        cd = 0
        n,m = len(matrix), len(matrix[0])
        output = []
        visited = set()
        for _ in range(m*n):
            output.append(matrix[cr][cc])
            visited.add((cr,cc))
            tc, tr = cc, cr
            cc+= direction[cd][1]
            cr+= direction[cd][0]
            if 0<=cc<m and 0<=cr<n and (cr, cc) not in visited:
                visited.add((cr,cc))
            else:
                cd = (cd+1) % 4
                cc= tc + direction[cd][1]
                cr= tr+ direction[cd][0]

        return output
