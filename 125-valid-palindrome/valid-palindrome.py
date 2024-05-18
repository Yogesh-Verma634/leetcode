class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        li = list(s)

        for idx, char in enumerate(s):
            if char == ' ' or not char.isalnum():
                li[idx] = ''
        
        li =  ''.join(li)
        
        print(li)
        left = 0
        right = len(li) -1 

        while left <= right:
            if li[left] != li[right]:
                return False
            left += 1
            right -= 1
        
        return True
            
        