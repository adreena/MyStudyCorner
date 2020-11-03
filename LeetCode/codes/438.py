# time O(n)
# space O(1)
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_count = [0]*26
        p_count = [0]*26
        for c in p:
            p_count[ord(c)-ord('a')]+=1
        output = []
        for i in range(len(s)):
            s_count[ord(s[i])-ord('a')]+=1
            if i >= len(p):
                s_count[ord(s[i-len(p)])-ord('a')]-=1
                
            if s_count == p_count:
                output.append(i-len(p)+1)
        return output