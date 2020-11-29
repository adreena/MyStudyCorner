"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        new_head = Node(-1,None, None, None)
        new_head.next = head
        def helper(node):
            if not node:
                return None
            
            
            if node.child:
                nxt = node.next
                child = helper(node.child)
                node.next = child
                child.prev = node
                while child and child.next:
                    child = child.next
                node.child=None
                if nxt:
                    child.next = helper(nxt)
                    nxt.prev = child
            elif node.next:
                node.next = helper(node.next)
            return node
        
        helper(head)
            
        return new_head.next