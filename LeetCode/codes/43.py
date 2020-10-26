# time O(NM)
# space: O(N+M)


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        output = [0 for i in range(len(num1)+len(num2))]
        k= len(output)-1
        for j in range(len(num2)-1,-1,-1):
            sub = 0
            carry = 0
            idx = k
            for i in range(len(num1)-1,-1,-1):
                temp= int(num2[j])* int(num1[i])+carry
                output[idx] += temp
                carry=output[idx] //10
                output[idx]%=10
                idx-=1
            if carry:
                output[idx] = carry
            k-=1
        while output and output[0]==0:
            output.pop(0)
        if not output:
            return "0"
        return ''.join([str(x) for x in output])