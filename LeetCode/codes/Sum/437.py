# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.paths = 0
        def helper(node, cur_sum):
            if node:
                new_sums = [node.val]+ [i+node.val for i in cur_sum]
                # print(cur_sum, new_sums)
                self.paths+=new_sums.count(sum)
                helper(node.left,  new_sums)
                helper(node.right, new_sums)
        helper(root, [])
        return self.paths