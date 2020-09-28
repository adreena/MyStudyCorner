# time O(logN)
# stack O(logN) call stack
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.pos = [-1,-1]
        def helper(left, right, nums, target):
            if left<=right:
                mid = (left+right) // 2
                if target < nums[mid]:
                    helper(left, mid-1, nums, target)
                elif target>nums[mid]:
                    helper(mid+1, right, nums, target)
                else:
                    if self.pos[0] == -1:
                        self.pos = [mid,mid]
                    else:
                        self.pos = [min(mid, self.pos[0]), max(mid, self.pos[1])]
                    helper(left, mid-1, nums, target)
                    helper(mid+1, right, nums, target)
        helper(0,len(nums)-1,nums,target)      
        return self.pos