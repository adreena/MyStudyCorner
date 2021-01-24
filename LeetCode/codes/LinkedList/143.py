# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        
        first = head
        slow = head
        fast = head
        prev = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        if prev:
            prev.next = None
            
        # rever second
        second = slow
        temp = second
        while temp and temp.next:
            nxt = temp.next
            temp.next = temp.next.next
            nxt.next = second
            second = nxt
        
        while second and first and first.next:
            f = first.next
            s = second.next
            first.next = second
            second.next = f
            
            second = s
            first = f
        first.next = second
        return first
            
            
            