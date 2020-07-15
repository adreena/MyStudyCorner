# time: O(max(nlogn, nm)) 
# space: O(n)

from collections import defaultdict
def longestStrChain(self, words: List[str]) -> int:
    words.sort(key=lambda x: len(x))
    wordchain = defaultdict(lambda:0)
    for word in words:
        wordchain[word]=1

    for word in words:
        for i in range(len(word)):
            key = word[:i]+word[i+1:]
            if key in wordchain:
                wordchain[word] = max(wordchain[key]+1, wordchain[word])
    return max(list(wordchain.values()))
