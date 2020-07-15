# time: O(N+L) length of word, N word
# space: O(N+L)
from collections import defaultdict
def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
    words = defaultdict(lambda:set())
    for word in wordList:
        for i in range(len(word)):
            key = word[:i]+'*'+word[i+1:]
            words[key].add(word)
    parents = defaultdict(lambda:set())
    depth = defaultdict(lambda:0)
    q = [(beginWord, 0)]
    depth[beginWord] = 1
    while len(q)>0:
        top , d = q.pop(0)
        for i in range(len(top)):
            key = top[:i] + '*'+top[i+1:]
            for nxt in words[key]:
                parents[nxt].add(top)
                if nxt not in depth:
                    q.append((nxt, d+1))
                    depth[nxt] = depth[top]+1
    outputs = []
    for parent in parents[endWord]:
        q = [(parent, [parent, endWord])]
        while len(s)>0:
            cur, path = q.pop(0)
            if cur == beginWord:
                if len(path) == depth[endWord]:
                    outputs.append(path)
            for p in parents[cur]:
                if depth[p]<depth[cur]:
                    q.append((p, [p]+path))
    return outputs
