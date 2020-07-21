# time : O(n)
# space: O(n)
def minRemoveToMakeValid(self, s: str) -> str:
    opens = 0
    balance = 0
    first = []
    for c in s:
        if c == '(':
            opens+=1
            balance+=1
        elif c == ')':
            if balance==0:
                continue
            balance-=1
        first.append(c)
    
    keep = opens - balance
    ans = []
    for c in first:
        if c == '(':
            if keep ==0:
                continue
            keep-=1
        ans.append(c)
    return ''.join(ans)