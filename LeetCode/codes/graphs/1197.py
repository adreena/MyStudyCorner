#2 methods are provided


class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        def helper(a,b):
            if a>=0 and b>=0:
                return [(a-2,b-1),(a-1,b-2)]
            elif a>=0 and b<=0:
                return [(a-2,b+1),(a-1,b+2)]
            elif a<=0 and b>=0:
                return [(a+1,b-2),(a+2,b-1)]
            else:
                return [(a+1,b+2),(a+2,b+1)]
        if x == 1 and y == 1:
            return 2
        q=[(x,y,0)]
        visited = set()
        visited.add((x,y))
        while q:
            i,j,d = q.pop(0)
            if i==0 and j==0:
                return d
            for ni,nj in helper(i,j):
                if(ni,nj) not in visited:
                    visited.add((ni,nj))
                    q.append((ni,nj,d+1))
        
#----
class Solution:
    def helper(self, cx, cy, tx, ty):
        if cx<=tx and cy<=ty:
            return [(cx+2,cy+1), (cx+1,cy+2)]
        elif cx<=tx and cy>=ty:
            return [(cx+2,cy-1), (cx+1, cy-2)]
        elif cx>=tx and cy>=ty:
            return [(cx-1,cy-2), (cx-2, cy-1)]
        else:
            return [(cx-1, cy+2), (cx-2, cy+1)]
       
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 1 and y == 1:
            return 2
        cx = 0
        cy = 0
        q = [(cx,cy,0)]
        visited = {(0,0)}
        while len(q)>0:
            cx, cy, d = q.pop(0)
            if cx == x and cy == y:
                return d
            for nx, ny in self.helper(cx,cy, x,y):
                if (nx, ny) not in visited:
                    q.append((nx,ny,d+1))
                    visited.add((nx,ny))