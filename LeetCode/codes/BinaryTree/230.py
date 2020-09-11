# time O(n)
# space: O(logn)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root is None:
            return None
        self.count = 1
        self.match = None
        def helper(node,k):
            if node and self.match is None:
                if node.left:
                    helper(node.left,k)
                if self.count == k:
                    self.match = node.val
                self.count+=1
                if node.right:
                    helper(node.right,k)
        helper(root,k)
        return self.match
