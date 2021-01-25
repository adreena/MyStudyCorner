class TrieNode:
    def __init__(self):
        self.children = {}
        self.last= False

class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = TrieNode()

        for word in words:
            cur = self.root
            w = word[::-1]
            for c in w:
                if c not in cur.children:
                    cur.children[c]=TrieNode()
                cur = cur.children[c]
            cur.last = True

        self.stream = deque()
    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.stream.appendleft(letter)
        cur = self.root
        for c in self.stream:
            if cur.last :
                return True
            if c in cur.children:
                cur = cur.children[c]
            else:
                return cur.last
        return cur.last



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
