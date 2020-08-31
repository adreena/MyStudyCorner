# time: O(N)
# space: O(N)

from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = [[root,0]]
        output=defaultdict(lambda:[])
        while q:
            top, d = q.pop(0)
            output[d].append(top.val)
            if top.left:
                q.append([top.left, d+1])
            if top.right:
                q.append([top.right, d+1])
                
        for i  in range(len(output)):
            if i % 2 == 1:
                output[i].reverse()
        return output.values()
                