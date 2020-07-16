# time: O(N)
# space: O(N)


def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

    temp_stack = []
    j=0
    for i in range(len(pushed)):
        temp_stack.append(pushed[i])
        while len(temp_stack)>0 and popped[j]==temp_stack[-1]:
            temp_stack.pop()
            j+=1
    if j != len(popped) or len(temp_stack)!=0:
        return False
    return True
