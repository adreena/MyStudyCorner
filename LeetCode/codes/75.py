# time O(N)
# space O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx_0 = 0
        
        for i in range(len(nums)):
            if nums[i]==0:
                nums[idx_0], nums[i]= nums[i], nums[idx_0]
                idx_0+=1
        for i in range(idx_0,len(nums)):
            if nums[i]==1:
                nums[idx_0], nums[i]= nums[i], nums[idx_0]
                idx_0+=1
        return nums