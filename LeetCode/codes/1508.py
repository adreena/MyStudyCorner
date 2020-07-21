# time: O(N)
# space: O(N)
def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for i in range(len(tokens)):
        val = None
        if len(tokens[i])>1:
            if tokens[i][0]=='-':
                val = int(tokens[i])
            elif tokens[i][0]=='+':
                val = int(tokens[i])
        if val or tokens[i].isdigit():
            stack.append(int(tokens[i]))
        elif tokens[i] in ['+', '-', '/', '*']:
            b = int(stack.pop())
            a = int(stack.pop())
            if tokens[i]=='*':
                stack.append(a*b)
            elif tokens[i]=='+':
                stack.append(a+b)
            elif tokens[i] == '-':
                stack.append(a-b)
            elif tokens[i] =='/':
                stack.append(a/b)
    return int(stack[-1])