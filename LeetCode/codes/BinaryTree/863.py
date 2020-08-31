# time O(N)
# space O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        def set_parent(parent, node):
            if node:
                node.parent = parent
                set_parent(node, node.left)
                set_parent(node, node.right)
                
        set_parent(None, root)
        output = []
        q = [(target, 0)]
        visited = {target}
        while q:
            top, d = q.pop(0)
            visited.add(top)
            if d == K:
                output.append(top.val)
            if top.left and top.left not in visited:
                q.append([top.left, d+1])
            if top.right and top.right not in visited:
                q.append([top.right,d+1])
            if top.parent and top.parent not in visited:
                q.append([top.parent, d+1])
        return output
                
        
        
        
                