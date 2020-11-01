# time O(N)
# space O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        if len(s)==0:
            return True
        for j in range(len(t)):
            
            if i < len(s) and s[i]==t[j]:
                i+=1
            if i == len(s):
                return True
        return False