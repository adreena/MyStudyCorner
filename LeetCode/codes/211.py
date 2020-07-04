class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root
        for i, c in enumerate(word):
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            node.word = word[:i+1]
        node.end = True
    
    def search(self, word, word_idx, parent_node):
        # print(word, word_idx)
        if parent_node.end and word_idx == len(word):
            return True
        if word_idx < len(word):
            if word[word_idx] == '.':
                res = False
                for c in parent_node.children:
                    res |= self.search(word, word_idx+1, parent_node.children[c])
                return res
            elif word[word_idx] not in parent_node.children:
                    return False
            else:
                return self.search(word, word_idx+1, parent_node.children[word[word_idx]])
        return False
                
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        self.trie.insert(word)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        
        res =  self.trie.search(word, 0, self.trie.root)
        return res
