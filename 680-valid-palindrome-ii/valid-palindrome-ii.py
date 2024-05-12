class Solution:

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        def isPalindrome(p):
            left = 0
            right = len(p)-1

            while left <= right:
                if p[left] != p[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        while left <= right:
            if s[left] != s[right]:
                left_ignored_word = s[:left] + s[left+1:]
                right_ignored_word = s[:right] + s[right+1:]
                return isPalindrome(left_ignored_word) or isPalindrome(right_ignored_word)
            left += 1
            right -= 1

        return True


    

        