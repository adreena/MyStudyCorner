# time O(N)
# space O(N)

import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        m = len(nums)
        output = []
        lefts = []
        rights = []
        cur_max = nums[0]
        for i in range(m):
            if i %k ==0:
                lefts.append(nums[i])
            else:
                lefts.append(max(lefts[-1], nums[i]))
                
        for i in range(m-1, -1, -1):
            if i+1 == len(nums) or (i+1)%k==0:
                rights.append(nums[i])
            else:
                rights.append(max(nums[i], rights[-1]))
        rights = rights[::-1]

        
        for i in range(m-k+1):
            output.append(max(lefts[i+k-1], rights[i]))
        return output