class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r] 
        res = 0
        while l < r:
            if height[l] < height[r]:
                res += min(max_l, max_r) - (height[l])
                l += 1
                max_l = max(max_l, height[l])
            else:
                res += min(max_l, max_r) - (height[r])
                r -= 1
                max_r = max(max_r, height[r])
        
        return res