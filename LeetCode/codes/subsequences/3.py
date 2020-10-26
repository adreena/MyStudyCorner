# time O(N)
# space O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        idx = defaultdict(lambda:-1)
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            if c in idx and idx[c]>=start:
                start = idx[c]+1
            idx[c] = i
            max_len = max(max_len, i-start+1)
        return max_len