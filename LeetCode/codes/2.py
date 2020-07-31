# time: O(N)
# space: O(N)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = None
        output = None
        carry = 0
        while l1 or l2:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            temp = v1 + v2 + carry
            carry = temp// 10
            temp %=10
            if output is None:
                output = ListNode(temp)
                head = output
            else:
                output.next = ListNode(temp)
                output = output.next
        if carry:
            output.next = ListNode(carry)
        
        return head