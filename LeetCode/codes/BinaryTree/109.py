# time: O(N)
# space: O(logN)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def find_half(node):
            slow = node
            fast = node
            prev_slow = None
            while slow and fast and fast.next:
                prev_slow = slow
                slow = slow.next
                fast = fast.next.next
            if prev_slow :
                prev_slow.next = None
            return slow
        
        def divide(node):
            if node is None:
                return None
            if node.next is None:
                return TreeNode(node.val)
            left = node
            middle = find_half(node)
            
            right = middle.next
            root = TreeNode(middle.val)
            root.left = divide(left)
            root.right = divide(right)
            return root
        
        return divide(head)