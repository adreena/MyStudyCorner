# time: O(n)
# space: O(n2)

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.grid = [['' for i in range(n)] for j in range(n)]
        

    def move(self, row: int, col: int, player_id: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        def check_win(player_id, row, col):
            count_row, count_col, count_d1, count_d2 = 0, 0, 0, 0
            for i in range(len(self.grid)):
                count_col+= 1 if self.grid[row][i] == player_id else 0
                count_row+= 1 if self.grid[i][col] == player_id else 0
                count_d1+= 1 if self.grid[i][i] == player_id else 0
            for i in range(len(self.grid)-1, -1, -1):
                count_d2+= 1 if self.grid[len(self.grid)-i-1][i] == player_id else 0

            if count_row == len(self.grid) or count_col == len(self.grid) or count_d1 == len(self.grid) or count_d2==len(self.grid):
                return True
            return False
        
        self.grid[row][col] = player_id
        if check_win(player_id, row, col):
            return player_id   
        return 0
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)