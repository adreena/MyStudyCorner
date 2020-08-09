# time :O(n)
# space: O(n)

def subarraySum(self, nums: List[int], k: int) -> int:
    dp = defaultdict(lambda:0)
    total = 0
    output = 0
    for num in nums:
        total+=num
        if total-k in dp:
            output+=dp[total-k]
        if total ==k:
            output+=1
        dp[total]+=1
    return output
