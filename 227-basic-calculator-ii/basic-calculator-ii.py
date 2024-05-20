class Solution:
    def calculate(self, s: str) -> int:

        operators = set(['+', '-', '*', '/'])
        num = 0
        pre_op = '+'
        stack = []
        s += '+'

        for ch in s:
            if ch == ' ':
                continue
            elif ch not in operators:
                num = num * 10 + int(ch)
            else:
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    operant = stack.pop()
                    stack.append(operant*num)
                else:
                    operant = stack.pop()
                    stack.append(int(operant/num))
                num = 0
                pre_op = ch
        
        return sum(stack)