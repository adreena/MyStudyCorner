
# time: O(nlogn)
# space: O(n)

from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_len = 0
        keys = set(list(counter.keys()))
        for key in counter.keys():
            if key+1 in keys:
                max_len = max(max_len, counter[key+1]+counter[key])
        return max_len