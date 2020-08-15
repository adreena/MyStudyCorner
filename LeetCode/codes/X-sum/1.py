# time: O(n)
# space: (n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if len(nums)==0:
            return [-1,-1]
        
        other = {}
        for i, num in enumerate(nums):
            other[target-num]= i
            
        for i, num in enumerate(nums):
            if num in other and i!=other[num]:
                return [i, other[num]]
        return [-1, -1]