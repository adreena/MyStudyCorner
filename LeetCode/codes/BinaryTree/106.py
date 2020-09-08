# note should build right first
#time O(N)
# space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        self.inorder_idx = {x:i for i, x in enumerate(inorder)}
        self.postorder = postorder
        def build_tree(left_idx, right_idx):
            if left_idx<=right_idx:
                node = TreeNode(self.postorder.pop())
                node_idx = self.inorder_idx[node.val]
                node.right = build_tree(node_idx+1,right_idx)
                node.left = build_tree(left_idx, node_idx-1)
                return node
            return None
        return build_tree(0,len(inorder)-1)