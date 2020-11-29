# O(MN3^L)
# space O(MN3^L)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.visited=set()
        self.n, self.m = len(board), len(board[0])
        def dfs(ci,cj,out, word_idx,word):
            # print(ci, cj, out, word_idx)
            if word_idx == len(word):
                return True
            self.visited.add((ci,cj))
            for ni,nj in [(ci,cj+1),(ci,cj-1),(ci-1,cj),(ci+1,cj)]:
                if 0<=ni<self.n and 0<=nj<self.m and (ni,nj) not in self.visited and word[word_idx]==board[ni][nj]:
                    if dfs(ni,nj,out+board[ni][nj], word_idx+1, word):
                        return True
            self.visited.remove((ci,cj))
            return False
        
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j]==word[0]:
                    if dfs(i,j,board[i][j],1, word):
                        return True
        return False