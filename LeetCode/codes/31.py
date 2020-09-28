# time O(N)
# space O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        
        m = len(nums)
        i =  m -2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
            
        if i <0:
            nums[:] = nums[::-1]
            return nums
        

        j = m-1
        while j >0:
            if nums[j]>nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                break
            j-=1
        
        nums[i+1:] = nums[i+1:][::-1]
        return nums