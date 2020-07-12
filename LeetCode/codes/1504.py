# time O(NM)
# space O(N)



def numSubmat(self, mat: List[List[int]]) -> int:
    count = 0
    for i, row in enumerate(mat):
        if i >0:
            for j in range(len(row)):
                if row[j]>0:
                    row[j]+= mat[i-1][j]
        stack = [-1]
        sub = 0
        for j in range(len(row)):
            while stack[-1]!=-1 and row[stack[-1]]>=row[j]:
                j0 = stack.pop()
                sub -= row[j0]*(j0-stack[-1])
            sub+=row[j]*(j-stack[-1])
            count+=sub
            stack.append(j)
    return count

