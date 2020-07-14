# time: O(N+L) length of word, N word
# space: O(N+L)

from collections import defaultdict

def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    wordMap = defaultdict(lambda:set())
    for word in wordList:
        for i in range(len(word)):
            key = word[:i]+'*'+word[i+1:]
            wordMap[key].add(word)
    q = [(beginWord,0)]
    visited = set()
    visited.add(beginWord)
    while len(q)>0:
        word, depth = q.pop(0)
        if word == endWord:
            return depth+1
        for i in range(len(word)):
            key = word[:i]+'*'+word[i+1:]
            for nxt in wordMap[key]:
                if nxt not in visited:
                    q.append((nxt, depth+1))
                    visited.add(nxt)
    return 0
