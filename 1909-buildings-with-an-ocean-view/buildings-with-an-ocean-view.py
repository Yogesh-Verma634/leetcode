class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_h = float('-inf')
        ocean_view_b = []
        for idx in range(len(heights)-1, -1, -1):
            if heights[idx] > max_h:
                ocean_view_b.append(idx)
                max_h = max(max_h, heights[idx])
        
        return ocean_view_b[::-1]
        