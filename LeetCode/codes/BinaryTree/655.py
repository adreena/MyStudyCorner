
# time O(N)
# space O(h + N) 
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        self.max_depth = 0
        def get_depth(node, d):
            if node:
                return max(get_depth(node.left,d+1),get_depth(node.right,d+1))+1
            return 0
        self.max_depth = get_depth(root,0)
        print(self.max_depth)

        self.min = 0
        self.max = 0
        self.depth = defaultdict(lambda:['' for i in range(2**self.max_depth -1)])
        def preorder(node, level, pos):
            self.min = min(self.min ,-level-1)
            self.max = max(self.max ,-level-1)
            self.depth[-level-1][pos] = str(node.val)
            if node.left:
                preorder(node.left, level-1, pos- 2**(level-1))
            if node.right:
                preorder(node.right,level-1, pos+ 2**(level-1))
                
        preorder(root, self.max_depth-1, 2**(self.max_depth-1) - 1)
        return [self.depth[i] for i in range(self.min, self.max)]