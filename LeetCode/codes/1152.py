# time O(MN2)
# space O(MN2)
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        dp = defaultdict(lambda:[])
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        patterns = defaultdict(lambda:0)
        for w in dp.values():
            combos = set(itertools.combinations(w, 3))
            for combo in combos:
                patterns[combo]+=1
        output = sorted(patterns,  key=lambda p: (-patterns[p], p))
        return output[0]