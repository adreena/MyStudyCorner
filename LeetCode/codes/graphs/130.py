# time O(NM)
# space O(1)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board)==0:
            return []
        n, m = len(board), len(board[0])
        border = {(i,j) for i in [0,n-1] for j in range(m)}
        border |={(i,j) for i in range(n)for j in [0,m-1]}
         
        # print('***', border)
        for i ,j in border:
            q = [(i,j)]
            while q:
                ci, cj = q.pop(0)
                if board[ci][cj]!='O':
                    continue
                board[ci][cj]='*'
                for ni,nj in [(ci-1,cj),(ci+1,cj),(ci,cj+1),(ci,cj-1)]:
                    if 0<=ni<n and 0<=nj<m and board[ni][nj]=='O':
                        q.append((ni,nj))
  
        for i in range(n):
            for j in range(m):
                if board[i][j]=='O':
                    board[i][j]='X'
                elif board[i][j]=='*':
                    board[i][j]='O'
        return board