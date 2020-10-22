# time O(nm)
# space: O(1)
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                count = 0
                for ni, nj in [(i+1,j),(i+1,j+1),(i+1,j-1), 
                               (i, j-1), (i, j+1),
                               (i-1,j),(i-1,j+1),(i-1,j-1)]:
                    if 0<=ni<len(board) and 0<=nj<len(board[0]):
                        if board[ni][nj] == 1 or board[ni][nj]=='d':
                            count+=1
                if board[i][j]==1:
                    if count <2 or count>3:
                        board[i][j] = 'd'
                else:
                    if count == 3:
                        board[i][j] = 'l'
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j]=='d':
                    board[i][j] = 0
                elif board[i][j]=='l':
                    board[i][j] = 1
        return board
                    
                    