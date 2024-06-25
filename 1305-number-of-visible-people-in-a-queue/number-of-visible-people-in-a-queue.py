class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = [] # contains height and number of people seen
        stack.append((heights[-1]))
        res = [0] * len(heights)

        for idx in range(len(heights)-2, -1, -1):
            height = heights[idx]
            count = 0
            while stack and height > stack[-1]:
                stack.pop()
                count += 1
            
            if stack:
                count += 1
                
            res[idx] = count
            stack.append((height))
    
        return res
