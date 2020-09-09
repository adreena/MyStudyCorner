# time O(n)
# space O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        new_head = ListNode(-1)
        new_head.next = head
        node = head
        while node and node.next:
            temp = node.next
            node.next = node.next.next
            temp.next = new_head.next
            new_head.next = temp
        
        return new_head.next