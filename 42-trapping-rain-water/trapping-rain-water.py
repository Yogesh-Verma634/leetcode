class Solution:
    def trap(self, height: List[int]) -> int:

        left_h = [0]
        right_h = [0]
        max_h = 0
        for idx in range(1, len(height)):
            max_h = max(height[idx-1], max_h)
            left_h.append(max_h)
        
        max_h = 0
        for idx in range(len(height)-2, -1, -1):
            max_h = max(height[idx+1], max_h)
            right_h.append(max_h)
        
        right_h = right_h[::-1]
        water = 0
        for idx in range(len(height)):
            curr_h = min(left_h[idx], right_h[idx]) - height[idx]
            if curr_h > 0:
                water += curr_h
        return water
        