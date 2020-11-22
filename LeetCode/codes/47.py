# time O(NN!)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        def backtrack(nums):
            if not nums:
                return []
            if len(nums)==1:
                return [nums]
            output = []
            for i in range(len(nums)):
                if i>0 and nums[i]==nums[i-1]:
                    continue
                keep = nums[i]
                rest = backtrack(nums[:i]+nums[i+1:])
                for r in rest:
                    output.append([keep]+r)
            return output
        
        return backtrack(nums)