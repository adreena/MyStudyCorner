class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if len(maze)==0:
            return False
        n,m = len(maze), len(maze[0])
        q= [start]
        visited = {(start[0],start[1])}
        while q:
            top = q.pop(0)
            # print(top)
            if top == destination:
                return True
            ci, cj = top
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ti, tj = ci+di, cj+dj
                while 0<=ti<n and 0<=tj<m and maze[ti][tj]==0 :
                    ti+=di
                    tj+=dj
                ti-=di
                tj-=dj
                if (ti,tj) not in visited:
                    visited.add((ti,tj))
                    q.append([ti,tj])
        return False