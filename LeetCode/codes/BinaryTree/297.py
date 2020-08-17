# time: O(N)
# space: O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.data = []
        def prefix(node):
            if node:
                self.data.append(node.val)
                prefix(node.left)
                prefix(node.right)
            else:
                self.data.append(None)
        prefix(root)
        return self.data

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        root = None
        def rebuild(data):
            if len(data):
                node = data.pop(0)
                if node is None:
                    return None
                root = TreeNode(node)
                root.left = rebuild(data)
                root.right = rebuild(data)
                return root
            return None
        root = rebuild(data)
        return root
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))