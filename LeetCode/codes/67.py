# time O(N)
# space O(N)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j = len(a)-1, len(b)-1
        carry = 0
        output = ""
        while i>=0 or j>=0:
            v1, v2 = 0, 0
            if i>=0:
                v1 = int(a[i])
                i-=1
            if j>=0:
                v2 = int(b[j])
                j-=1
            temp = v1+v2+carry
            if temp ==2:
                carry = 1
                output = '0'+output
            elif temp == 3:
                carry = 1
                output = '1'+output
            else:
                carry = 0
                output = str(temp)+output
        if carry==1:
            output = str(carry)+output
        return output
