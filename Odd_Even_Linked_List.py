class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        if not head or not head.next:
            return head
        
        odd = head
        even = odd.next
        evenhead = head.next
        
        while odd.next and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenhead
        return head
