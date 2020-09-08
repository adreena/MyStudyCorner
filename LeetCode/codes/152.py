
# time O(n)
# space O(n)

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dp = [[1,1] for i in range(len(nums))]
        max_prod = nums[0]
        dp[0] = [nums[0],nums[0]]
        for i in range(1,len(nums)):
            prods = [nums[i], nums[i]*dp[i-1][0], nums[i]*dp[i-1][1]]
            dp[i] = [min(prods),max(prods)]
            max_prod = max(max_prod, max(prods))
        return max_prod