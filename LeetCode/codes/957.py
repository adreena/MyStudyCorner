# time O(k, min(N, 2^k)) there are 2^k binary combination of states
# space O(k)

class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        dp = {}
        while N:
            key = tuple(cells)
            if key in dp:
                N = N%(dp[key]-N)
            dp[key]=N
            new_cells = [0 for i in range(len(cells))]
            for i in range(1,len(cells)-1):
                if cells[i-1]==cells[i+1]:
                    new_cells[i]=1
            cells = new_cells
            N-=1
        return cells