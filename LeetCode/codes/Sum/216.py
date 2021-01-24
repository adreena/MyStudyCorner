# time O(n,k)
# space O(k)

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = [i for i in range(1,10)]
        outputs = []
        def backtrack(idx, cur_sum , output):
            if cur_sum == n and len(output)==k:
                outputs.append(output)
            for i in range(idx, 9):
                if cur_sum+nums[i]<=n and len(output)+1 <=k:
                    backtrack(i+1, cur_sum+nums[i], output+[nums[i]])
        
        backtrack(0,0,[])
        return outputs