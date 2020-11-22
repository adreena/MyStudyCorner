class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        
        cur_sum = 0
        dp = defaultdict(lambda:0)
        dp[0]=1
        count = 0
        for i in range(len(A)):
            cur_sum+=A[i]
            cur_sum%=K
            if cur_sum in dp:
                count+=dp[cur_sum]
            dp[cur_sum]+=1
        # print(dp)
        return count
            