# time O(N)
# space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<=j:
            skip = False
            if not s[i].isalpha() and not s[i].isdigit():
                i+=1
                skip=True
            if not s[j].isalpha() and not s[j].isdigit():
                j-=1
                skip=True
            if not skip:
                if s[i].lower()==s[j].lower():
                    i+=1
                    j-=1
                else:
                    return False
        return True
