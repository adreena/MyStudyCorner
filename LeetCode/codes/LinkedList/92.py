# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        count = 1
        temp_head = head
        prev = None
        while head and count<m:
            count+=1
            prev = head
            head = head.next
        
        # start reverse
        while count<n and head.next:
            nxt = head.next
            head.next = nxt.next
            if prev:
                nxt.next = prev.next
                prev.next=nxt
            else:
                nxt.next = temp_head
                temp_head = nxt
            count+=1
        return temp_head
            