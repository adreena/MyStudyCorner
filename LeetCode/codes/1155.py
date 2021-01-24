
# space O(df)
# time O(df)
from collections import defaultdict
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        outputs =0
        mod = 10**9 +7
        memo = defaultdict(lambda:0)
        def backtrack(num_d, f, target, current):
            
            if num_d ==0 and current == target:
                return 1
            if num_d == 0 or current == target:
                return 0
            if (num_d, current) not in memo:
                count = 0
                for i in range(1,f+1):
                    if current+i <=target:
                        count += backtrack(num_d-1, f, target, current+i)
                memo[(num_d, current)] = count%mod
            return memo[(num_d, current)]
            
        return backtrack(d, f, target, 0)