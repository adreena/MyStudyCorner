# time O(N)
# space O(1)
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp = set(nums)
        if 1 not in temp:
            return 1

        for i  in range(len(nums)):
            if nums[i]<=0 or nums[i]>len(nums):
                nums[i] = 1
        for i in range(len(nums)):
            idx = abs(nums[i])
            if idx == len(nums):
                nums[0] = -1*abs(nums[0])
            else:
                nums[idx] = -abs(nums[idx])

        for i in range(1, len(nums)):
            if nums[i]>0:
                return i
        if nums[0] >0:
            return len(nums)
        return len(nums)+1
