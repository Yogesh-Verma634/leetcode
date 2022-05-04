'''
Given the head of a singly linked list, reverse the list, and return the reversed list.


Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''

### Iterative solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head
        
        while curr:
            
            # reverse the prev and curr node
            nxt = curr.next
            curr.next = prev
            prev = curr
            
            curr = nxt
            
        return prev
      
#### Recursive solution

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head:
            return None
        
        newHead = head
        
        # on reaching last node, return newHead so that we can get newHead to point at the end of the list
        if not head.next:
            return newHead
        
        # keep calling recursively till we reach the last node, so that we can apply reverse logic from behind the list
        newHead = self.reverseList(head.next)
        
        # Reverse the two nodes -> head and head.next
        head.next.next = head
        head.next = None
        
        # return the last node after reversal, don't return head since it points to null, i.e. newHead => 5 -> 4 -> null and head => 4 -> null
        return newHead
