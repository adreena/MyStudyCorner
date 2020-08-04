# time: O(n2)
# space: O(n)
def maximalRectangle(self, matrix: List[List[str]]) -> int:
    max_area = 0
    m = len(matrix)
    if m ==0:
        return 0
    n = len(matrix[0])
    left = [0 for _ in range(n)]
    right = [n for _ in range(n)]
    height = [0 for _ in range(n)]
    for i in range(m):
        cur_left = 0
        cur_right = n
        for j in range(n):
            if matrix[i][j] == '1':
                left[j] = max(left[j],cur_left)
                height[j]+=1
            else:
                cur_left= j+1
                left[j]=0
                height[j] = 0

        for j in range(n-1, -1, -1):
            if matrix[i][j] == '1':
                right[j] = min(cur_right, right[j])
            else:
                cur_right = j
                right[j] = n
        for l, h, r in zip(left, height, right):
            max_area = max(max_area, h*(r-l))
    return max_area
