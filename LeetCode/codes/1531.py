# time O(2^N)
# space O(N) its the deepest recursion call 
class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        memo = defaultdict(lambda:0)
        def backtrack(i, c, cur_len, rem_k):
            if i == len(s):
                return 0
            
            key = (i,c,cur_len, rem_k)
            if key in memo:
                return memo[key]
            
            del_cost = float('inf')
            keep_cost = 0
            if rem_k>0:
                del_cost = backtrack(i+1, c, cur_len, rem_k-1)
            
            if c == s[i]:
                extra_cost = 0
                if cur_len == 1 or len(str(cur_len+1))>len(str(cur_len)):
                    extra_cost=1
                keep_cost = extra_cost + backtrack(i+1, c, cur_len+1, rem_k)
            else:
                keep_cost = 1 + backtrack(i+1, s[i], 1, rem_k)
            memo[key] = min(keep_cost, del_cost)
            return memo[key]
        
        return backtrack(0,'',0,k)