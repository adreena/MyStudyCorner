class Solution:
    def wordBreak(self, st: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        q= [(0,[])]
        paths=[]
        def check(s):
            dp = [False for i in range(len(s)+1)]
            dp[0]=True
            for i in range(1,len(s)+1):
                for j in range(i):
                    if s[j:i] in words and dp[j]:
                        dp[i]=True
            return dp[-1]
        def dfs(s, path):
            if not s:
                paths.append(' '.join(path))
            elif check(s):
                for i in range(1,len(s)+1):
                    if s[:i] in words:
                        dfs(s[i:], path+[s[:i]])
        dfs(st,[])
        return paths