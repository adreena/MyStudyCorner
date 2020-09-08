
#time O(N)
# space O(1)

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        t = set(T)
        start =0
        min_len = float('inf')
        count = 0
        i = 0
        output = ''
        while i< len(S):
            if S[i] ==T[count]:
                count+=1
            if count == len(T):
                end = i
                count-=1
                while count>=0:
                    if S[i] == T[count]:
                        count-=1
                    i-=1
                i+=1
                count+=1
                if end-i+1<min_len:
                    min_len = end - i+1
                    output = S[i:end+1]
            i+=1
        return output