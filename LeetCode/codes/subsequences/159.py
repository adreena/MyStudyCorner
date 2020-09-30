# time O(N)
# space O(1)
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        max_len = 0
        start = 0
        last_idx = OrderedDict()
        for i,c in enumerate(s):
            if c in last_idx:
                del last_idx[c]
            last_idx[c] = i
            if len(last_idx) > 2:
                _, idx = last_idx.popitem(last=False)
                start = idx+1
            max_len = max(max_len, i-start+1)
        return max_len
                
                