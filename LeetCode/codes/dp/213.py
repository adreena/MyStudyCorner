# time O(N)
# space O(N)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[0]
        
        dp = [0 for i in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i-1])
        
        max1 = dp[-1]
        dp = [0 for i in range(len(nums))]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return max(dp[-1],max1)