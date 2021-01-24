# time O(N+M)
# space O(N+M)
from collections import Counter, defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_count = Counter(t)
        s_count = defaultdict(lambda:0)
        
        char_count = 0
        start_idx = -1
        min_len = float('inf')
        start = 0
        for i, c in enumerate(s):
            s_count[c]+=1
            if c in t_count and s_count[c]<=t_count[c]:
                char_count+=1
            if char_count == len(t):
                while s[start] not in t_count or s_count[s[start]]>t_count[s[start]]:
                    # if  s_count[s[start]]>t_count[s[start]]:
                    s_count[s[start]]-=1
                    if s_count[s[start]]<=0:
                        del s_count[s[start]]
                    start+=1
                if i-start+1<min_len:
                    min_len = i-start+1
                    start_idx=start
        if start_idx == -1:
            return ""
        return s[start_idx:start_idx+min_len]