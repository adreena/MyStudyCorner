# time: O(n2)
# space: O(n2)

def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    temp_sum = {}
    for i in range(len(A)):
        for j in range(len(B)):
            temp_sum[A[i]+B[j]]=temp_sum.get(A[i]+B[j], 0)+1
            
    output = 0
    for i in range(len(C)):
        for j in range(len(D)):
            temp = C[i]+D[j]
            output+= temp_sum.get(-temp, 0)
    return output