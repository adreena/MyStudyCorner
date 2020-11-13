class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        output = []
        def check(r,c):
            
            for i in range(c):
                if board[r][i]=='Q':
                    return False
            for i,j in zip(range(r,-1,-1), range(c,-1,-1)):
                if board[i][j]=='Q':
                    return False
            for i,j in zip(range(r,n,1), range(c,-1,-1)):
                if board[i][j]=='Q':
                    return False
            return True
        
        def convert(b):
            temp = []
            for r in b:
                temp.append(''.join(r))
            return temp
        
        def backtrack(col, count):
            for row in range(n):
                if check(row, col):
                    board[row][col]='Q'
                    count+=1
                    if col+1 == n:
                        if count==n:
                            output.append(convert(board))
                    else:
                        backtrack(col+1,count)
                    count-=1
                    board[row][col]='.'
        
        for col in range(n):
            board= [['.' for i in range(n)] for j in range(n)]
            backtrack(col,0)
        
        return output