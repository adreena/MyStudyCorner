# time: O(N2)
# space: O(N)

def countSquares(self, matrix: List[List[int]]) -> int:
    dp = [0 for i in range(len(matrix[0])+1)]
    squares = 0
    for i in range(len(matrix)):
        new_dp = [0 for i in range(len(matrix[0])+1)]
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                new_dp[j+1] = min(dp[j+1], dp[j], new_dp[j])+1
        dp = new_dp
        squares+= sum(dp)
    return squares
