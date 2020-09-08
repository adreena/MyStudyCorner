# time O(N)
# space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca = None
        def helper(node, p, q):
            if node is None:
                return False
            f = False
            if node == p or node == q:
                f = True
            l = helper(node.left,p,q)
            r = helper(node.right,p,q)
            if sum([l,f,r])>=2:
                self.lca = node
            return l or r or f
    
        helper(root,p,q)
        return self.lca
                