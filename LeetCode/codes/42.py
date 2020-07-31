
#time: O(N)
# space: O(N)

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left = [0 for i in range(len(height))]
        right = [0 for i in range(len(height))]
        left[0] = height[0]
        right[-1]= height[-1]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
        for i in range(len(height)-2, -1, -1):
            right[i] = max(right[i+1], height[i])
        
        water = 0
        for l,r, h in zip(left, right, height):
            water += min(l,r)-h
        return water
        