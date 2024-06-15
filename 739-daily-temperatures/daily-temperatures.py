class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0 for _ in range(len(temperatures))]

        for idx, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                val, popped_idx = stack.pop()
                res[popped_idx] = idx - popped_idx
            stack.append((temp, idx))

        return res

        