# time O(N)
# space O(N)

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        self.cache = defaultdict(lambda:None)
        def copy(node):
            if node is None:
                return None
            if node in self.cache:
                return self.cache[node]
            node_copy = Node(node.val)
            self.cache[node] = node_copy
            node_copy.next = copy(node.next)
            node_copy.random = copy(node.random)
            return node_copy
    
        return copy(head)