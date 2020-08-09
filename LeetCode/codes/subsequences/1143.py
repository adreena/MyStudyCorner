# time O(nm)
# space O(nm)

from collections import Counter
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        max_len = 0
        for i in range(1, m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
                max_len = max(max_len, dp[i][j])
        return dp[i][j]