
# time: O(nlogn)
# space: O(n)

from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        print(envelopes)
        def LIS(nums):
            dp = []
            for i in range(len(nums)):
                idx = bisect_left(dp, nums[i])
                if idx == len(dp):
                    dp.append(nums[i])
                else:
                    dp[idx] = nums[i]
            return dp
        ans = LIS([e[1] for e in envelopes])
        print(ans)
        return len(ans)
        
        

