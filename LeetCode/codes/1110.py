# time : O(N)
# space: recursion stack O(N) + forest O(N)

def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
    self.forest = []
    def helper(node, parent, to_delete):
        if node is None:
            return None
        if node.val in to_delete:
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

            helper(node.left, None, to_delete)
            helper(node.right, None, to_delete)
        else:
            if parent is None:
                self.forest.append(node)
            helper(node.left, node, to_delete)
            helper(node.right, node, to_delete)
    helper(root, None, to_delete)
    return self.forest
