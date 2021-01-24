# time: O(N)
# space: O(N)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        output = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            output[i] = nums[i-1]*output[i-1]
        
        
        temp = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            output[i] *= temp
            temp*=nums[i]
        return output