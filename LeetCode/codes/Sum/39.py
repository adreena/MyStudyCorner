# time O(N*(target_sum/min_val)
# space: O(N*(target/min))

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.outputs = set()
        candidates.sort()
        def helper(candidates, idx, cur_sum, target_sum, output):
            if cur_sum == target_sum:
                self.outputs.add(tuple(sorted(output)))
            for i in range(idx, len(candidates)):
                if cur_sum+candidates[i] <= target_sum:
                    helper(candidates, i, cur_sum+candidates[i], target_sum, output+[candidates[i]])
        helper(candidates, -1, 0, target, [])
        return self.outputs
