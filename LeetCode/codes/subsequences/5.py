
# time: O(n2)
# space: O(n2)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)==0:
            return ''
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(dp)):
            dp[i][i] = True
        
        max_len = 1
        start =0
        k = 0
        for i in range(len(dp)):
            k+=1
            for j in range(len(dp)-k):
                if s[j] == s[j+k]:
                    if k == 1 or dp[j+1][j+k-1]:
                        dp[j][j+k] = True
                        if k+1>max_len:
                            start = j
                            max_len = k+1
        return s[start:start+max_len]
        