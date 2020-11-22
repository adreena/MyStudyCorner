class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        
        def helper(node, cur_sum):
            if node:
                if node.left is None and node.right is None and cur_sum+node.val == sum:
                    return True
                else:
                    return helper(node.left, cur_sum+node.val) or helper(node.right, cur_sum+node.val)
                
            return False
        
        return helper(root, 0)