# time: O(nlogn)
# space: O(n)
from bisect import bisect_left
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda x: x[1])
        lis = []
        for pair in pairs:
            idx = bisect_left(lis, pair[0])
            if idx == len(lis):
                lis.append(pair[1])
        return len(lis)