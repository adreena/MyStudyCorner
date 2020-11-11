# time O(N)
# space: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        output = defaultdict(lambda:None)
        if not root:
            return []
        q=[(root,0)]
        max_d=0
        while q:
            top, d = q.pop(0)
            max_d = max(d,max_d)
            if d not in output:
                output[d]=top.val
            if top.right:
                q.append((top.right,d+1))
            if top.left:
                q.append((top.left,d+1))
        
        # print(output)
        return [output[key] for key in range(max_d+1)]