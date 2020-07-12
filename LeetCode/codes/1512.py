# time : O(min(N^k, N^(N-k)) N choose K
# space: O(min(N^k , N^(N-k)))

from itertools import combinations
from collections import defaultdict

def numIdenticalPairs(self, nums: List[int]) -> int:
    x = defaultdict(lambda:[])
    for i , a in enumerate(nums):
        x[a].append(i)
    total = 0
    for k, v in x.items():
        combs = list(combinations(v, 2))
        total+= len(combs)
    return total