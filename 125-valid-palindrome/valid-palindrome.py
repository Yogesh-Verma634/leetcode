class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        li = list(s)

        s = [ch for ch in s.lower() if ch.isalnum()]
        li =  ''.join(s)
        
        left, right = 0,  len(li) -1 

        while left <= right:
            if li[left] != li[right]:
                return False
            left += 1
            right -= 1
        
        return True
            
        