# time O(N)
# space O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        if head is None:
            return None
        def helper():
            slow, fast = head, head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                if fast is None:
                    return None
                if fast == slow:
                    return fast
            return None
    
        intersection = helper()
        if not intersection:
            return None
        x = head
        while x!=intersection:
            x = x.next
            intersection = intersection.next
        return intersection