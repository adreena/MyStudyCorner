# time O(N)
# space O(N)
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.paths = []
        def helper(node, path):
            if node:
                if node.left is None and node.right is None:
                    self.paths.append('->'.join(path+[str(node.val)]))
                else:
                    helper(node.left, path+[str(node.val)])
                    helper(node.right, path+[str(node.val)])
        helper(root, [])
        return self.paths
