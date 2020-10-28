# time O(n)
# space O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        dp = [0 for i in range(len(nums)+1)]
        for i in range(1, len(nums)+1):
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
        return dp[-1]