# time O(N)
# time O(N)
# space O(1)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        tempA = headA
        tempB= headB
        while tempA:
            lenA+=1
            tempA= tempA.next
        while tempB:
            lenB+=1
            tempB = tempB.next
            
        if lenA<lenB:
            headA, headB = headB, headA
            lenA, lenB = lenB, lenA
        
        i = 0
        while i < lenA-lenB:
            headA = headA.next
            i+=1
        while headA and headB:
            if headA!=headB:
                headA = headA.next
                headB = headB.next
            else:
                return headA
        return None