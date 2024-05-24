class Solution:
    def trap(self, height: List[int]) -> int:

        right_h = [0]
        max_h = 0
        for idx in range(len(height)-2, -1, -1):
            max_h = max(height[idx+1], max_h)
            right_h.append(max_h)
        right_h = right_h[::-1]

        water = 0
        max_h = 0
        for idx, h in enumerate(height):
            curr_h = min(right_h[idx], max_h) - height[idx]
            if curr_h > 0:
                water += curr_h
            max_h = max(max_h, h)
        return water
        