# Time: O(N) length of a path
# Space: O(M) M directoties

from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict()
    def get(self, token):
        return self.children.get(token,None )
    def setdefault(self, token):
        return self.children.setdefault(token, TrieNode())

class FileSystem:

    def __init__(self):
        self.dirs = TrieNode()
        self.files = defaultdict(str)

    def ls(self, path: str) -> List[str]:
        dirs = path.split('/')
        if path in self.files:
            return dirs[-1:]
        
        cur_dir = self.dirs
        for d in dirs:
            if d and cur_dir:
                cur_dir = cur_dir.get(d)
        if cur_dir: return sorted(cur_dir.children.keys())
        return []

    def mkdir(self, path: str) -> None:
        dirs = path.split('/')
        cur_dir = self.dirs
        for d in dirs:
            if d: cur_dir = cur_dir.setdefault(d)
            
    def addContentToFile(self, filePath: str, content: str) -> None:
        self.mkdir(filePath)
        self.files[filePath]+=content

    def readContentFromFile(self, filePath: str) -> str:
        return self.files[filePath]

