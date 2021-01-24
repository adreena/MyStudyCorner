
# O(N2^N)
#space O(N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        def backtrack(s, output):
            if not s:
                result.append(output)
            
            for i in range(1,len(s)+1):
                if s[:i]==s[:i][::-1] :
                    backtrack(s[i:],output+[s[:i]])
        backtrack(s,[])
        return result
        