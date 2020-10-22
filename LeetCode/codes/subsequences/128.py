# time O(N)
# space O(N)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set= set(nums)
        max_len = 0
        for i in range(len(nums)):
            if nums[i]-1 not in num_set:
                curr = nums[i]
                curr_len = 1
                while curr+1 in num_set:
                    curr_len+=1
                    curr = curr+1
                max_len = max(max_len, curr_len)
        return max_len