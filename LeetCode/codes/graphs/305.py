# time O(nm)
# space O(nm)
class UnionFind:
    def __init__(self):
        self.parents={}
        self.sizes = {}
        self.count = 0
    
    def insert(self,r,c):
        if (r,c) in self.parents:
            return
        self.parents[(r,c)] = (r,c)
        self.sizes[(r,c)] = 1
        self.count+=1
    
    def find_root(self,i):
        while i!= self.parents[i]:
            self.parents[i]=self.find_root(self.parents[i])
            i = self.parents[i]
        return i
    
    def union(self,p,q):
        root_p, root_q = self.find_root(p), self.find_root(q)
        if root_p==root_q:
            return
        small, big = sorted([root_p, root_q], key=lambda x: self.sizes[x])
        self.sizes[big]+=self.sizes[small]
        self.parents[small] = big
        self.count-=1
        
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        islands = []
        uf = UnionFind()
        for r, c in positions:
            uf.insert(r,c)
            for nr, nc in [(r+1,c),(r,c+1),(r-1,c),(r,c-1)]:
                if 0<=nr<m and 0<=nc<n:
                    if (nr,nc) not in uf.parents:
                        continue
                    uf.union((r,c), (nr,nc))
            islands.append(uf.count)
        return islands
                