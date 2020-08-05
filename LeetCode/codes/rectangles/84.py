
# time: O(n2)
# space: O(n)

def largestRectangleArea(self, heights: List[int]) -> int:
    stack = [-1]
    max_rect = 0
    for i, height in enumerate(heights):
        while stack[-1]!=-1 and height<heights[stack[-1]]:
            h = heights[stack.pop()]
            max_rect = max(h*(i-stack[-1]-1), max_rect)
        stack.append(i)
    while stack[-1]!=-1:
        h = heights[stack.pop()]
        max_rect = max(h*(len(heights)-stack[-1]-1), max_rect)
    return max_rect