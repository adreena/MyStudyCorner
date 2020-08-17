# time: O(N)
# space: O(n)

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_idx = defaultdict(lambda:-1)
        for i , s in enumerate(S):
            last_idx[s] = i
        
        partitions = []
        i =0
        j = 0
        while i<len(S):
            j = i
            l = i
            while i<=j<len(S):
                j = max(last_idx[S[i]], j)
                i+=1
            partitions.append(i-l)
        return partitions