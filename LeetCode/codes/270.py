# Time: O(H)
# Space: O(H) height of the tree can be reduced to 1 if I use while instead of recursion


def closestValue(self, root: TreeNode, target: float) -> int:
    self.dist = float('inf')
    self.node = None
    def helper(root):
        if root:
            cur_dist = abs(root.val - target)
            if cur_dist < self.dist:
                self.dist = cur_dist
                self.node = root.val
            if target<=root.val:
                helper(root.left)
            else:
                helper(root.right)
    helper(root)
    return self.node