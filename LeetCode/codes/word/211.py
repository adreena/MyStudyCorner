# time: O(NM) number of keys*len of word to search
# space: O(N) # lenght of word to search for becuase chars are 26 and constant


class TrieNode:
    def __init__(self):
        self.children = {}
        self.last = False
        self.word = ''

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur_node = self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c] = TrieNode()
            cur_node = cur_node.children[c]
        cur_node.last = True
        cur_node.word = word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        def helper(word, cur_node):
            for i, c in enumerate(word):
                if c == '.':
                    for child in cur_node.children:
                        if helper(word[i+1:], cur_node.children[child]):
                            return True
                if c not in cur_node.children:
                    return False
                cur_node = cur_node.children[c]
            return cur_node.last
        return helper(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
