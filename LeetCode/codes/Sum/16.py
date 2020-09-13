# time O(n2)
#space: O(logn) space for search algorithm

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==0:
            return None
        self.closest_sum = float('inf')
        def twoSum(others, target, c):
            i,j = 0, len(others)-1
            while i<j:
                a,b = others[i], others[j]
                temp_sum = a+b+c
                diff1 = abs(temp_sum-target)
                diff2 = abs(self.closest_sum - target)
                if diff1<diff2:
                    self.closest_sum = temp_sum
                if temp_sum<target:
                    i+=1
                elif temp_sum>target:
                    j-=1
                else:
                    break
        nums.sort()
        for i in range(len(nums)):
            twoSum(nums[i+1:], target, nums[i])
        
        return self.closest_sum