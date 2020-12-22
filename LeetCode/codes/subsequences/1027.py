# time O(N2)
# space O(N2)
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = {i:{} for i in range(len(A))}
        maxlen = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                if diff in dp[j]:
                    dp[i][diff]=dp[j][diff]+1
                else:
                    dp[i][diff]=1
                maxlen = max(dp[i][diff], maxlen)
        # print(dp)
        return maxlen+1