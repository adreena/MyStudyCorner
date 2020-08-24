# O(nlogn)
# O(N)
from collections import defaultdict, Counter
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dp = defaultdict(lambda:[])
        for t, u, w in sorted(zip(timestamp,username,website)):
            dp[u].append(w)
        patterns = defaultdict(lambda: 0)
        for w in dp.values():
            combos = set(itertools.combinations(w, 3))
            for c in combos:
                patterns[c]+=1
        output = sorted(patterns, key=lambda x:(-patterns[x], x))
        return output[0]