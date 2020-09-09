# time O(N)
# space: O(1)
class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        
        for i in range(len(s)-1,-1,-1):
            num = ord(s[i])-ord('A')+1
            total+= num*26**(len(s)-i-1)
        return total
            