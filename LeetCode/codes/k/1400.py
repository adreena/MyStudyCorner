# time O(N)
# space O(N)
class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        s_count = Counter(s)
        odds = 0
        for key,val in s_count.items():
            if val % 2 == 1:
                odds+=1
        if odds>k:
            return False
        
        if k <= len(s):
            return True
        
        return False