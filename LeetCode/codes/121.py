
# time O(N)
# space O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0
        max_profit = 0
        min_buy = prices[0]
        
        for i in range(1, len(prices)):
            max_profit = max(prices[i]-min_buy, max_profit)
            min_buy = min(min_buy, prices[i])
            
        return max_profit