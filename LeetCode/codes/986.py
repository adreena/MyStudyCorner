# time O(N)
# space O(1)
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        output = []
        while i <len(A) and j <len(B):
            s1,e1 = A[i]
            s2,e2 = B[j]
            # print(output)
            if s2<=e1<=e2:
                output.append([max(s1,s2), min(e1,e2)])
            elif s1<=e2<=e1:
                output.append([max(s1,s2), min(e1,e2)])
            if e1<=e2:
                i+=1
            else:
                j+=1
        return output