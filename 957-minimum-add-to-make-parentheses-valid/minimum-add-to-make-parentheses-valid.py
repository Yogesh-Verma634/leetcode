class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            
            if c == ')':
                if not stack:
                    count += 1
                else:
                    stack.pop()

            else:
                stack.append(c)
        
        return count + len(stack)


                
        