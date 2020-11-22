class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        cur_sum =0
        min_len = len(nums)+1
        for i in range(len(nums)):
            cur_sum+=nums[i]
            while cur_sum>=s:
                if cur_sum-nums[start]>=s:
                    cur_sum-=nums[start]
                    start+=1
                else:
                    break
            if cur_sum>=s:
                min_len = min(min_len, i-start+1)
        
        if min_len == len(nums)+1:
            return 0
        return min_len