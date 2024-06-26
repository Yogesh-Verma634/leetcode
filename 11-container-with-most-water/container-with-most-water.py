class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        l, r = 0, len(height)-1

        water = 0

        while l < r:
            area = min(height[l], height[r]) * (r - l)
            water = max(water, area)

            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return water