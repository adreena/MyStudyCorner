# time O(E+V)
# space O(V+E)
# each clique is 1 transaction

class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        deg = defaultdict(lambda:0)
        for x, y, amount in transactions:
            deg[x]-=amount
            deg[y]+=amount
        
        non_zeros = sorted([a for k, a in deg.items() if a!=0])
        
        def BFS(nums):
            q = [[nums[0], [0]]]
            while q:
                cur_sum , path = q.pop(0)
                if cur_sum==0:
                    nonzeros = [nums[i] for i in range(len(nums)) if i not in set(path)]
                    return  nonzeros
                for nxt in range(path[-1]+1, len(nums)):
                    q.append([cur_sum+nums[nxt], path+[nxt]])
        
        trans = len(non_zeros)
        while non_zeros:
            non_zeros = sorted(BFS(non_zeros))
            trans-=1
        return trans