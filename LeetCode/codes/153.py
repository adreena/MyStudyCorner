# time O(logn)
# space O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1
        min_val = float('inf')
        while left<=right:
            mid = (left+right+1)//2
            if nums[left]<nums[mid]:
                min_val = min(min_val, nums[left])
                left = mid+1
            else:
                min_val = min(min_val, nums[mid])
                right = mid-1
        return min_val
    