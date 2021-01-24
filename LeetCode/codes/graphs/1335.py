# time O(dN2)
# space: O(N)

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty)<d:
            return -1
        
        n = len(jobDifficulty)
        dp = [float('inf') for i in range(n+1)]
        dp[-1]=0
        
        for k in range(1, d+1):
            # print('k', k, n-k+1)
            for i in range(n-k+1):
                max_d = 0
                dp[i]=float('inf')
                for j in range(i,n-k+1):
                    max_d = max(max_d, jobDifficulty[j])
                    dp[i]=min(dp[i], max_d+dp[j+1])
                    print(dp)
                print('***')
        return dp[0]