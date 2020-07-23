# time: O(H , worst case N)
# space: O(N)

def kthSmallest(self, root: TreeNode, k: int) -> int:
	stack = []
	while True :
	    
	    while root:
	        stack.append(root)  
	        root = root.left
	    root = stack.pop()
	    k-=1
	    if not k:
	        return root.val
	    root = root.right