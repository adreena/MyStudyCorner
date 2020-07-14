# time: O(NM)
# space: O(M)

def maximalSquare(self, matrix: List[List[str]]) -> int:
    if len(matrix) == 0:
        return 0
    dp = [0 for i in range(len(matrix[0])+1)]
    max_area = 0
    for i in range(len(matrix)):
        new_dp = [0 for i in range(len(matrix[0])+1)]
        for j in range(len(matrix[0])):
            if matrix[i][j] == "1":
                new_dp[j+1] = min(new_dp[j], dp[j], dp[j+1]) +1
                max_area = max(max_area, new_dp[j+1]**2)
        dp = new_dp
    return max_area
