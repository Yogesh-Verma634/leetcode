'''
2207. Maximize Number of Subsequences in a String


Input: text = "abdcdbc", pattern = "ac"
Output: 4
Explanation:
If we add pattern[0] = 'a' in between text[1] and text[2], we get "abadcdbc". Now, the number of times "ac" occurs as a subsequence is 4.
Some other strings which have 4 subsequences "ac" after adding a character to text are "aabdcdbc" and "abdacdbc".
However, strings such as "abdcadbc", "abdccdbc", and "abdcdbcc", although obtainable, have only 3 subsequences "ac" and are thus suboptimal.
It can be shown that it is not possible to get more than 4 subsequences "ac" by adding only one character.
'''


class Solution:
    def maximumSubsequenceCount(self, s: str, p: str) -> int:
        if p[0] == p[1]:
            x = s.count(p[0])
            x += 1
            return x * (x - 1) // 2
        else:
            x = s.count(p[0])
            y = s.count(p[1])
            z = 0
            c = 0
            for i in s:
                if i == p[0]:
                    c += 1
                elif i == p[1]:
                    z += c
            return z + max(x, y)
          
'''
Credits: https://leetcode-cn.com/u/wwwwodddd/
'''
