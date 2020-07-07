# Time complexity O(NM^N)
# Space Complexity O(M)

def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    self.results= []
    def DFS(word, word_dict):
        word_dict.remove(word)
        if check(word, word_dict):
            self.results.append(word)
        word_dict.add(word)

    def check(word, word_dict):
        if word in word_dict:
            return True
        for i in range(len(word), 0, -1):
            if word[:i] in word_dict and check(word[i:], word_dict):
                return True
        return False

    word_dict = set(words)
    for word in words:
        DFS(word, word_dict)
    return self.results
    
    
