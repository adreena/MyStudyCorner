# time O(N2)
# space O(N2)
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        counter = defaultdict(lambda:{})
        ans = 0
        for i in range(len(A)):
            for j in range(i):
                diff = A[i]-A[j]
                if diff not in counter[j]:
                    counter[j][diff] = 1
                    
                if diff not in counter[i]:
                    counter[i][diff]=0
                
                
                counter[i][diff] = max(counter[i][diff], counter[j][diff]+1)
                ans = max(ans, counter[i][diff])
        return ans
                