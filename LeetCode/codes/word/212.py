#time: O(M*4^L-1) M size of the board each cell has 4 direcition and L length of the word
# space O(N) words in dictionary

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.word = None
class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.output = set()
    
    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.end = True
        cur.word = word

    def searchDFS(self, parent, i, j, board):
        temp = board[i][j]
        board[i][j] = ''
        parent = parent.children[temp]
        if parent.end:
            self.output.add(parent.word)
        for ni, nj in [(i+1,j),(i-1,j),(i, j+1), (i, j-1)]:
            if 0<=ni<len(board) and 0<=nj<len(board[0]) and board[ni][nj] in parent.children:
                self.searchDFS(parent, ni, nj, board)
            
        board[i][j] = temp
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie.root.children:
                    trie.searchDFS(trie.root, i, j, board)
        return trie.output
        
        