
#time: O(n2^n)
# space: O(n2^n)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums)==1:
            return [[], nums]
        
        
        num = nums[0]
        rest = self.subsets(nums[1:])
        temp = []
        for r in rest:
            temp.append(r+[num])
        return temp + rest