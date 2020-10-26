# time O(2^N)
# space O(2^N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        self.memo = {0:[], 1:[TreeNode(0)]}
        def DFS(n):
            if n not in self.memo:
                path = []
                for i in range(n):
                    j = n-i-1
                    for left in DFS(i):
                        for right in DFS(j):
                            node = TreeNode(0)
                            node.left = left
                            node.right = right
                            path.append(node)
                self.memo[n] = path
            return self.memo[n]
        return DFS(N)