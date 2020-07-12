# Time: O(N2)
# Space: O(N)
                                  
def numSub(self, s: str) -> int:

    count = 0
    sub = 0
    stack = [-1]
    r = [int(s[i]) for i in range(len(s))]
    for i in range(len(r)):
        while stack[-1]!=-1 and r[stack[-1]]>=r[i]:
            j = stack.pop()
            sub -= r[j]*(j-stack[-1])
        sub+=r[i]*(i-stack[-1])
        count+=sub
        stack.append(i)
    return count % (pow(10,9) +7)