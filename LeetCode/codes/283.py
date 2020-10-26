# time O(N)
# space : O(1)

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_idx = 0
        
        i=0
        while i < len(nums):
            if nums[i]!=0:
                nums[write_idx] = nums[i]
                write_idx+=1
            i+=1
        while write_idx<len(nums):
            nums[write_idx] = 0
            write_idx+=1
        return nums