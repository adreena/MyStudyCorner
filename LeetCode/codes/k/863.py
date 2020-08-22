# time: O(N)
# space: O(N)

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        
        def set_parent(node, parent):
            if node:
                node.parent = parent
                set_parent(node.left, node)
                set_parent(node.right, node)
        
        set_parent(root, None)
        
        q = [(target,0)]
        visited = {target}
        output = []
        while q:
            node, depth = q.pop(0)
            if depth == K:
                output.append(node.val)
            for nxt in [node.left, node.right, node.parent]:
                if nxt and nxt not in visited:
                    visited.add(nxt)
                    q.append([nxt, depth+1])
        return output