# time O(n)
# space O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        stack = []
        output = defaultdict(lambda:0)
        count = 0
        while head:
            while stack and stack[-1][0]<head.val:
                x,i = stack.pop()
                output[i]=head.val
            stack.append((head.val, count))
            head = head.next
            count+=1
        while stack:
            _,i = stack.pop()
            output[i]=0
        return [output[k] for k in range(count)]
