# time O(Nsqrt(n))
# space O(sqrt(N))
class Solution:
    def numSquares(self, n: int) -> int:
        sqaures = [i**2 for i in range(int(math.sqrt(n))+1)]
        dp = [float('inf') for i in range(n+1)]
        dp[0] = 0
        
        for i in range(1, len(dp)):
            for s in sqaures:
                if s<=i:
                    dp[i] = min(dp[i], dp[i-s]+1)
                else:
                    break
        return dp[-1]