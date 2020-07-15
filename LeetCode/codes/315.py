# time: O(N) in the worst case all nodes line up in 1 path
# space: O(N)
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.count = 0
        self.right = None
        self.left = None

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def helper(node, num, size):
            if node is None:
                return TreeNode(num), size
            if num < node.val:
                node.count+=1
                node.left, size = helper(node.left, num, size)
            else:
                if num>node.val:
                    size+=1
                node.right, size = helper(node.right, num, size+node.count)
            return node, size

        output = []
        root = None
        for num in nums[::-1]:
            root, size = helper(root, num, 0)
            output = [size]+output

        return output
