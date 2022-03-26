class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        
        p = 1
        lo, hi = 0, len(nums) -1
        
        # if there are more than one element between low and high, mid will always lie in between
        # and not be lo or hi
        # This prevents mid to be on the ends
        while lo < hi-1:  
            mid = (lo + hi) // 2

            prev = nums[mid-1]
            nxt = nums[mid+1]
                
            curr = nums[mid]
            if curr > prev and curr > nxt:
                return mid
            
            elif curr < prev:
                hi = mid - 1
            elif curr < nxt:
                lo = mid + 1
        
        return left if nums[left] >= nums[right] else right
