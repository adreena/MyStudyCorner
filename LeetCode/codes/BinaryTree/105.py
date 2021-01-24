# time O(N)
# space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        self.inorder = defaultdict(lambda:-1)
        for i, num in enumerate(inorder):
            self.inorder[num]=i
            
        def helper(preorder,left, right):
            if left<right:
                val = preorder.pop(0)
                node = TreeNode(val)
                node_loc = self.inorder[val]
                node.left=helper(preorder, left, node_loc)
                node.right=helper(preorder,node_loc+1, right)
                return node
            return None
        
        return helper(preorder,0,len(preorder))