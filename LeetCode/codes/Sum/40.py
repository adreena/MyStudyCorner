# O(n* (target/min_val))
# O(target/min)
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        outputs = []
        candidates.sort()
        visited = set()
        def helper(idx, nums, cur_sum, output):
            
            if cur_sum == target:
                outputs.append(output)
            for i in range(idx, len(nums)):
                if i>idx and nums[i]==nums[i-1]:
                    continue
                if cur_sum+nums[i]<=target:
                    helper(i+1, nums, cur_sum+nums[i], output+[nums[i]])
        helper(0, candidates, 0, [])
        return outputs