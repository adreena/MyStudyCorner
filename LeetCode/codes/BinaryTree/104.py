# time O(N)
# space O(N)

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        s = [(root,1)]
        max_d = 0
        while s:
            top, d = s.pop()
            max_d = max(d, max_d)
            if top.left:
                s.append((top.left, d+1))
            if top.right:
                s.append((top.right, d+1))
        return max_d