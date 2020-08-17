
#time: O(N2)
#space:O(N)

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        q = [0]
        visited = set()
        while q:
            cur = q.pop(0)
            if cur == len(s):
                return True
            visited.add(cur)
            for j in range(cur,len(s)):
                temp = s[cur:j+1]
                if j+1 not in visited and  temp in wordDict:
                    q.append(j+1)
                    visited.add(j+1)
        return False