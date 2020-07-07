# Time: O(M+N)
# Space: O(1)
    
def searchMatrix(self, matrix, target):
    i = len(matrix)-1
    j = 0
    while i >=0 and j < len(matrix[0]):
        if target == matrix[i][j]:
            return True
        if target>matrix[i][j]:
            j+=1
        else:
            i-=1
    return False