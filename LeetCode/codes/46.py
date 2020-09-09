#time O(n!)
# space O(n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        temp = []
        for i in range(len(nums)):
            keep = nums[i]
            rest = self.permute(nums[:i]+nums[i+1:])
            for r in rest:
                temp.append([keep]+r)
        return temp