# time O(N)
# space O(logn)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        self.max_sum = float('-inf')
        def helper(node):
            if node is None:
                return 0
            
            left = helper(node.left)
            right = helper(node.right)
            self.max_sum = max(self.max_sum, left+right+node.val, node.val+max(right,left), node.val)
            return max([node.val+max(right,left), node.val])
        
        helper(root)
        return self.max_sum