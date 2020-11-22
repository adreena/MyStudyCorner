# time : O(n)
# space: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        def refine(s,_open, _close):
            balance = 0
            new_s=[]
            for i in range(len(s)):
                if s[i]==_open:
                    balance+=1
                elif s[i]==_close:
                    if balance == 0:
                        continue
                    balance-=1
                new_s.append(s[i])
            return new_s
        
        s = refine(s, '(', ')')
        s = refine(s[::-1], ')', '(')
        return ''.join(s[::-1])