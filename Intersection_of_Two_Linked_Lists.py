class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        l1, l2 = headA, headB
        
        while l1 or l2:
            
            if not l1:
                l1 = headB
            elif not l2:
                l2 = headA
                
            if l1 == l2:
                return l2
            
            l1 = l1.next
            l2 = l2.next
            
        return None
