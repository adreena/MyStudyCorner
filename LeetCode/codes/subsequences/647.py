# time O(n2)
# space: O(n2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        counts=0
        dp = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            counts+=1
            
        k = 0
        for i in range(len(s)):
            k+=1
            for j in range(len(s)-k):
                if s[j] == s[j+k]:
                    if k ==1 or dp[j+1][j+k-1]:
                        dp[j][j+k]=True
                        counts+=1
        return counts