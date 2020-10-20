
# space O(df)
# time O(df)
from collections import defaultdict
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        self.memo = defaultdict(lambda:0)
        self.mod = 10**9 + 7
        def backtrack(d_count, target_sum, f):
            if d_count == 0 and target_sum==0:
                return 1
            if d_count == 0 or target_sum == 0:
                return 0
            if (d_count, target_sum) not in self.memo:
                count = 0
                for i in range(1,f+1):
                    if target_sum>=i:
                        count+=backtrack(d_count-1, target_sum-i, f)
                self.memo[(d_count,target_sum)] = count%self.mod
            
            return self.memo[(d_count, target_sum)]
    
        return backtrack(d, target, f)