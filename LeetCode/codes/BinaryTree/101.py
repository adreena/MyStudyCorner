# time O(N)
# space O(logn)
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def is_mirror(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return node1.val == node2.val and is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)
        return is_mirror(root, root)
