
# time: O(M2N)
# space: O(M2N)

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordDict = defaultdict(lambda:set())
        for word in wordList:
            for i in range(len(word)):
                key = word[:i]+'*'+word[i+1:] # O(M) extra for making string
                wordDict[key].add(word)
        
        q = [(beginWord, 0)]
        visited = {beginWord}
        while q:
            top, d = q.pop(0)
            if top == endWord:
                return d+1
            for i in range(len(top)):
                key = top[:i]+'*'+top[i+1:]
                for nxt in wordDict[key]:
                    if nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, d+1))
        return 0