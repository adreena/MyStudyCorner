# time O(N^(target_sum/min_val)
# space: O(target/m)

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        outputs = []
        candidates.sort()
        def helper(idx, output, cur_sum):
            if cur_sum == target:
                outputs.append(output)
            for i in range(idx,len(candidates)):
                if cur_sum+candidates[i]<=target:
                    helper(i, output+[candidates[i]], cur_sum+candidates[i])
        
        helper(0,[], 0)
        return outputs