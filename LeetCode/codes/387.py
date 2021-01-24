# time O(n)
# space O(1) only 26 charss
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c]==1:
                return i
        return -1
