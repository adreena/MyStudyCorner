# time: O(N2)
# space: O(N)

def decodeString(self, s: str) -> str:
    chars = []
    nums = []
    for i in range(len(s)):
        if s[i].isdigit():
            temp = int(s[i])
            if i>0 and s[i-1].isdigit():
                temp = nums.pop()*10+temp
            nums.append(temp)
        else:
            temp = s[i]
            if s[i]==']':
                temp = ''
                while len(chars)>0 and chars[-1]!='[':
                    temp = chars.pop() + temp
                chars.pop() # pop '['
                temp = temp*nums.pop()
            chars.append(temp)
    return ''.join(chars)
