class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ### Hashset solution
        count_char_s = {}
        count_char_t = {}

        for ch in s:
            if ch not in count_char_s:
                count_char_s[ch] = 0
            count_char_s[ch] += 1 
        
        for ch in t:
            if ch not in count_char_t:
                count_char_t[ch] = 0
            count_char_t[ch] += 1 

        return count_char_s == count_char_t
        ### Sorting solution, TC - N(log N), SC - O(1)
        return sorted(s) == sorted(t)
        