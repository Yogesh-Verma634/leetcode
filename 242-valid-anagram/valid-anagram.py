class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        ### HashMap solution, TC - O(N), SC - O(N)
        count_char_s = {}

        for ch in s:
            if ch not in count_char_s:
                count_char_s[ch] = 0
            count_char_s[ch] += 1 
        
        for ch in t:
            if ch not in count_char_s:
                return False
            count_char_s[ch] -= 1
            if not count_char_s[ch]:
                del(count_char_s[ch])

        return True if not len(count_char_s) else False
        ### Sorting solution, TC - N(log N), SC - O(1)
        # return sorted(s) == sorted(t)
        