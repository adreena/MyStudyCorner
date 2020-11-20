#  O(1)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        outputs=[]
        def helper(section, idx, output):
            # print(output, idx, len(s))
            if section==4 and idx == len(s):
                outputs.append(output)
            elif section<4:
                for i in range(idx, len(s)):
                    cur = s[idx:i+1]
                    if output and output[-1]!='.':
                            output+='.'
                    if cur == '0':
                        helper(section+1, i+1, output+'0')
                        break
                    else:
                        if 1<=int(cur)<=255:
                            helper(section+1, i+1, output+cur)
        helper(0, 0, '')
        return outputs