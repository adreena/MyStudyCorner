#time O(NM)
# space O(1)
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if len(rooms)==0:
            return rooms
        n, m = len(rooms), len(rooms[0])
        for i in range(n):
            for j in range(m):
                if rooms[i][j] == 0:
                    q= [(i,j,0)]
                    while q:
                        ci, cj , d = q.pop(0)
                        for ni, nj in [(ci+1,cj),(ci-1,cj),(ci,cj+1),(ci,cj-1)]:
                            if 0<=ni<n and 0<=nj<m and rooms[ni][nj]!=-1:
                                if rooms[ni][nj]>d+1:
                                    rooms[ni][nj] = d+1
                                    q.append((ni,nj,d+1))
        return rooms
        