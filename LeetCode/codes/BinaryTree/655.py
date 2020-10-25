
# time O(N)
# space O(h + N) 
class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        
        def get_depth(node):
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right))+1
        
        depth = get_depth(root)
        self.output = defaultdict(lambda:["" for i in range(2**depth -1)])
        def print_tree(node, depth, pos):
            if node:
                self.output[depth][pos] = str(node.val)
                if node.left:
                    print_tree(node.left, depth-1, pos-2**(depth -1))
                if node.right:
                    print_tree(node.right, depth-1, pos+2**(depth-1 ))
                    
                    
        print_tree(root, depth-1 , 2**(depth-1)-1)
        return [self.output[key] for key in range(depth-1,-1,-1)]