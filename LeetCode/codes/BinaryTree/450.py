#Time O(h)
# space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def helper(node, key):
            if node is None:
                return None
            if node.val == key:
                if node.left is None and node.right is None:
                    return None
                if node.right:
                    nxt_node = node.right
                    while nxt_node and nxt_node.left:
                        nxt_node = nxt_node.left
                    node.val = nxt_node.val
                    node.right = helper(node.right, node.val)
                elif node.left:
                    nxt_node = node.left
                    while nxt_node and nxt_node.right:
                        nxt_node = nxt_node.right
                    node.val = nxt_node.val
                    node.left = helper(node.left, node.val)
            elif node.val>key:
                node.left = helper(node.left, key)
            else:
                node.right = helper(node.right, key)
            return node
        return helper(root, key)
