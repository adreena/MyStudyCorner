
# time: O(N)
# space: O(n)

class Solution:
    def calculate(self, s: str) -> int:
        def postfix(s):
            ops = []
            nums= []
            priority = {')':-1, '(':-1, '+':0, '-':0, '*':1, '/':1}
            for i in range(len(s)):
                if s[i].isdigit():
                    cur = int(s[i])
                    if i-1>=0 and s[i-1].isdigit():
                        prev = nums.pop()
                        cur = prev*10+cur
                    nums.append(cur)
                else:
                    while ops and priority[ops[-1]]>=priority[s[i]]:
                        nums.append(ops.pop())
                    ops.append(s[i])
            while ops:
                nums.append(ops.pop())
            return nums
        
        s = ''.join(s.split())
        # print(s)
        postfix_s = postfix(s)
        # print(postfix_s)
        stack = []
        for i in range(len(postfix_s)):
            if str(postfix_s[i]).isdigit():
                stack.append(postfix_s[i])
            else:
                x, y = stack.pop(), stack.pop()
                if postfix_s[i] == '+':
                    stack.append(y+x)
                elif postfix_s[i] == '-':
                    stack.append(y-x)
                elif postfix_s[i] == '*':
                    stack.append(y*x)
                elif postfix_s[i] == '/':
                    stack.append(y//x)
        return stack[-1]