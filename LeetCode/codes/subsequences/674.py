# time: O(n)
# space: O(1)


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        max_len = 1
        start =0
        count = 1
        for i, num in enumerate(nums):
            if i>0:
                if num>nums[i-1]:
                    count+=1
                else:
                    count = 1
                if count>max_len:
                    max_len = count
                    start = i-count+1
        return len(nums[start:start+max_len])
        