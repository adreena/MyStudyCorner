
#time: O(n2)
# space: O(n) without the output

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, target):
            output = set()
            i = 0
            j = len(nums)-1
            while i<j:
                temp = nums[i]+nums[j]
                if temp==target:
                    output.add(tuple(sorted([nums[i],nums[j]])))
                    i+=1
                    j-=1
                elif temp<target:
                    i+=1
                else:
                    j-=1
            return output
        
        result = set()
        nums.sort()
        for i in range(len(nums)):
            temp_result = twoSum(nums[i+1:], -nums[i])
            while temp_result:
                x, y = temp_result.pop()
                result.add(tuple(sorted([nums[i], x, y])))
        return result