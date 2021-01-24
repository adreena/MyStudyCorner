class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        if len(A)==0:
            return 0
        
        # mark islands
        n,m = len(A), len(A[0])
        bfs = []
        def mark_first():
            for i in range(n):
                for j in range(m):
                    if A[i][j]==1:
                        A[i][j]=-1
                        q= [(i,j)]
                        bfs.append((i,j))
                        while q:
                            ci,cj = q.pop(0)
                            for ni, nj in [(ci+1,cj),(ci-1,cj),(ci,cj+1),(ci,cj-1)]:
                                if 0<=ni<n and 0<=nj<m:
                                    if A[ni][nj]==1:
                                        A[ni][nj]=-1
                                        q.append((ni,nj))
                                        bfs.append((ni,nj))
                        return
        mark_first()
        # for r in A:
        #     print(r)
        
        step = 0
        while bfs:
            new_bfs= []
            for ci, cj in bfs:
                for ni, nj in [(ci+1,cj),(ci-1,cj),(ci,cj+1),(ci,cj-1)]:
                    if 0<=ni<n and 0<=nj<m:
                        if A[ni][nj]==0:
                            A[ni][nj]=-1
                            new_bfs.append((ni,nj))
                        elif A[ni][nj]==1:
                            return step
            bfs = new_bfs
            step+=1
        