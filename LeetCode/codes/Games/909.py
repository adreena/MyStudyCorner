# tim eO(NM)
# space O(NM)

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n,m = len(board), len(board[0])
        
        def get_index(val):
            a, rem = divmod(val-1,n)
            i = n-1-a
            j = rem if i%2!=n%2 else n-1-rem
            return i,j
        
        visited = {0}
        
        q = [(1, 0)]
        while q:
            cell, moves = q.pop(0)
            if cell == n*n:
                return moves
            visited.add(cell)
            for nxt in range(cell+1,min(cell+6,n*m)+1):
                i, j = get_index(nxt)
                if board[i][j]!=-1:
                    nxt = board[i][j]
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, moves+1))
        return -1


                
                
                
            
        