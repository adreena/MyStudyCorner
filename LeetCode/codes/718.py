# Similar to finding regex pattern
# time: O(NM)
# space O(NM)

def findLength(self, A: List[int], B: List[int]) -> int:
    dp = [[ 0 for _ in range(len(B)+1)] for j in range(len(A)+1)]
    max_len = 0
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]+1

    for r in dp:
        max_len = max(max(r), max_len)
    return max_len

