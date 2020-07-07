# Time: O(N) all of the nodes
# Space: O(H) height of the tree


def countNodes(self, root: TreeNode) -> int:
    self.count = 0
    def helper(root):
        if root is None:
            return 0
        lefts = helper(root.left)
        rights = helper(root.right)
        return lefts+rights+1
    return helper(root)