# time O(logN)
# stack O(logN) call stack
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.min_idx , self.max_idx = -1, -1
        def helper(left, right, nums, target):
            if left<=right:
                mid = (left+right)//2
                if nums[mid] == target:
                    if self.min_idx==-1:
                        self.min_idx , self.max_idx = mid, mid
                    else:
                        self.min_idx = min(self.min_idx, mid)
                        self.max_idx = max(self.max_idx, mid)
                if target<=nums[mid]:
                    helper(left, mid-1, nums, target)
                if target>=nums[mid]:
                    helper(mid+1, right, nums, target)
                    
        helper(0, len(nums)-1, nums, target)
        return [self.min_idx, self.max_idx]