# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        new_head = ListNode(-1)
        new_head.next = head
        prev = new_head
        while head and head.next:
            x = head
            y = head.next
            nxt = head.next.next
            prev.next=y
            y.next = x
            x.next = nxt
            prev = x
            head = x.next
        
        return new_head.next
        