class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        valid_paren_str = ''
        stack = deque()

        for idx, char in enumerate(s):
            if char == '(':
                stack.append([(char, idx)])
            if char == ')':
                if not stack:
                    stack.append([(char, idx)])
                elif stack[-1][0][0] == '(':
                    stack.pop()
                else:
                    stack.append([(char, idx)])

        valid_paren_str = list(s)
        while stack:
            ele = stack.pop()
            valid_paren_str[ele[0][1]] = ''
        return ''.join(valid_paren_str)

        