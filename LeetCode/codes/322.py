#time O(MN)
#space O(M)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1 for i in range(amount+1)]
        dp[0]=0
        coins = set(coins)
        for i in range(amount+1):
            if i in coins:
                dp[i]=1
            else:
                for c in coins:
                    if c< i:
                        dp[i] = min(dp[i], dp[c]+dp[i-c])
        if dp[-1]== amount+1:
            return -1
        return dp[-1]
