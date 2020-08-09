# time: O(n2)
# space: O(n)

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s)<k:
            return 0
        
        min_char_count = min(set(s), key = s.count)
        if s.count(min_char_count)>=k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(min_char_count))