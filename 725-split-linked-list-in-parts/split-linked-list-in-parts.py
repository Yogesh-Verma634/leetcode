# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        LEN = 0
        len_cal = head
        res = []

        while len_cal:
            LEN += 1
            len_cal = len_cal.next

        bucket_size = LEN // k
        remainder = LEN % k

        prev = None 
        curr = head
        curr_bucket = []
        while curr:
            curr_bucket.append(head)
            for _ in range(bucket_size + (1 if remainder > 0 else 0)):
                prev = curr
                curr = curr.next

            prev.next = None
            head = curr
            remainder -= 1
        
        if len(curr_bucket) != k:
            for _ in range(k - len(curr_bucket)):
                curr_bucket.append(curr)

        return curr_bucket 
        
        