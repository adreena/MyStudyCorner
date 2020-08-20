
# time: O(n*m^2) m: length words
#space (nm2)

from collections import defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordDict = defaultdict(lambda:set())
        for word in wordList:
            for i in range(len(word)):
                key = word[:i]+'*'+word[i+1:]
                wordDict[key].add(word)
        
        parent = defaultdict(lambda:set())
        depth = defaultdict(lambda:0)
        
        q = [(beginWord, 0)]
        depth[beginWord]=1
        while q:
            top, d = q.pop(0)
            for i in range(len(top)):
                key = top[:i]+'*'+top[i+1:]
                for nxt in wordDict[key]:
                    if nxt != top:
                        if nxt not in depth:
                            depth[nxt] = depth[top]+1
                            q.append((nxt, depth[top]+1))
                        parent[nxt].add(top)
       
        paths = []
        for p in parent[endWord]:
            s = [[p, [p, endWord]]]
            while s:
                top, path = s.pop()
                if top == beginWord:
                    if len(path) == depth[endWord]:
                        paths.append(path)
                for nxt in parent[top]:
                    if depth[nxt]<depth[top]:
                        s.append([nxt, [nxt]+path])
        return paths
                        