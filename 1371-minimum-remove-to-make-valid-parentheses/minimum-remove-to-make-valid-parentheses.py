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

        invalid_idx = set()
        while stack:
            ele = stack.pop()
            invalid_idx.add(ele[0][1])
            
        for idx, char in enumerate(s):
            if idx not in invalid_idx:
                valid_paren_str += char

        return valid_paren_str

        