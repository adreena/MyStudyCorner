
# time O(n)
# space:O(1)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        cur_sum = nums[0]
        max_sum =nums[0]
        for i in range(1, len(nums)):
            cur_sum = max(cur_sum+nums[i], nums[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum