from collections import OrderedDict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        idx = OrderedDict()
        count = 0
        start = 0
        max_len = 0
        for i in range(len(s)):
            if s[i] in idx:
                del idx[s[i]]
            idx[s[i]] = i
            if len(idx) == k+1:
                _, j = idx.popitem(last=False)
                start = max(start, j+1)
            max_len = max(max_len, i-start+1)
        return max_len