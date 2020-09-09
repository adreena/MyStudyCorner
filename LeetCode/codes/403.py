class Solution:
    def canCross(self, stones: List[int]) -> bool:
        self.visited = set()
        def dfs(stones, stone, k, path, stones_set):
            if (stone,k) in self.visited:
                return False
            if stone == stones[-1]:
                # print(path)
                return True
            for nxt_k in [k-1, k, k+1]:
                if nxt_k<=0:
                    continue
                if stone+nxt_k in stones_set:
                    if dfs(stones, stone+nxt_k, nxt_k, path+[stone+nxt_k], stones_set):
                        return True
            self.visited.add((stone,k))
            return False
        stones_set = set(stones)
        return dfs(stones, 0, 0, [0],stones_set)
            