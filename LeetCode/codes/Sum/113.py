# time O(N)
# space O(h)
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        self.paths = []
        def get_sum(node, path, path_sum, target_sum):
            if node:
                if node.left is None and node.right is None:
                    if path_sum+node.val == target_sum:
                        self.paths.append(path+[node.val])
                else:
                    get_sum(node.left, path+[node.val], path_sum+node.val, target_sum)
                    get_sum(node.right, path+[node.val], path_sum+node.val, target_sum)
        get_sum(root, [], 0, sum)
        return self.paths
