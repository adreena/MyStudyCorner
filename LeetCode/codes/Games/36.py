#time O(MN)
# space O(1)

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j] != '.':
                    current = board[i][j]
                    
                    if (i, current) in visited or (current,j) in visited or (i//3,j//3,current) in visited:
                        return False
                    visited.add((i,current))
                    visited.add((current,j))
                    visited.add((i//3,j//3,current))
        return True