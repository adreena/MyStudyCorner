class Solution:
    def calculate(self, s: str) -> int:
        def convert_postfix(s):
            ops = []
            output = []
            prev_sign = 1
            sign = 1
            priorities = {'(':-1, ')':-1, '+':0, '-':0, '*':1, '/':1}
            for i in range(len(s)):
                if s[i]=='+' or s[i]=='-':
                    if i == 0 or s[i-1] in ['(','*','/']:
                        if s[i]=='-':
                            sign = -1
                        continue
                if s[i].isdigit():
                    temp = 0
                    if len(output)>0 and s[i-1].isdigit():
                        prev, prev_sign = output.pop()
                        temp = prev*10
                    temp+= int(s[i])
                    output.append((temp, prev_sign*sign))
                    sign = 1
                    prev_sign = 1
                else:
                    if s[i]==')':
                        while len(ops)>0 and ops[-1]!='(':
                            output.append((ops.pop(),1))
                        ops.pop()
                        continue
                    elif s[i]!='(':
                        while len(ops)>0 and priorities[s[i]]<=priorities[ops[-1]]:
                            output.append((ops.pop(), 1))
                    ops.append(s[i])
            while ops:
                output.append((ops.pop(),1))
            return output
        
        s = ''.join(s.split())
        s = convert_postfix(s)
        ans = []
        # print(s)
        for i, (p, sign) in enumerate(s):
            if p in ['+', '-','/','*']:
                b, a = ans.pop(), ans.pop()
                if p=='+':
                    ans.append(a+b)
                elif p=='-':
                    ans.append(a-b)
                elif p=='*':
                    ans.append(a*b)
                else:
                    ans.append(a//b)
            else:
                ans.append(sign*p)
        return ans[0]
                    