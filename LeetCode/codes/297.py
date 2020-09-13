# time O(n)
# space O(n)

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
        def helper(node):
            if node is None:
                self.data.append(None)
            else:
                self.data.append(node.val)
                helper(node.left)
                helper(node.right)
        helper(root)
        return self.data



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def rebuild(data):
            if len(data)>0:
                val = data.pop(0)
                if val is None:
                    return None
                node = TreeNode(val)
                node.left = rebuild(data)
                node.right = rebuild(data)
                return node
            return None

        root = rebuild(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
