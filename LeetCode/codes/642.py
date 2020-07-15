# time: O(N)
# space: O(N)
from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.sent = ''
        self.time = 0
        self.end = False

    def get(self, token):
        return self.children.get(token, None)

    def set(self, token):
        return self.children.setdefault(token, TrieNode())


class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.cur_node = self.root
        self.cur_prefix = ''
        for sentence, time in zip(sentences, times):
            self.insert(sentence, time)

    def insert(self, sentence, time):
        cur_node = self.root
        for c in sentence:
            cur_node.set(c)
            cur_node = cur_node.children[c]
        cur_node.sent = sentence
        cur_node.time += time
        cur_node.end = True

    def search(self, cur_node):
        self.matches = []
        def helper(cur_node):
            if cur_node.end:
                self.matches.append([cur_node.time,cur_node.sent])
            for c in cur_node.children:
                if cur_node.get(c):
                    helper(cur_node.children[c])
        helper(cur_node)
        self.matches.sort(key=lambda x: (-x[0], x[1]))
        return  [x for y, x in self.matches[:3]]

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.insert(self.cur_prefix, 1)
            self.cur_node = self.root
            self.cur_prefix = ''
            return None
        else:
            self.cur_prefix+=c
            if self.cur_node is None or not self.cur_node.get(c):
                self.cur_node = None
                return None
            self.cur_node=self.cur_node.get(c)
            return self.search(self.cur_node)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
