class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        start = last = float('-inf')
        def isPeak(prev, curr, next):
            return curr > prev and curr > next

        if len(nums) == 1:
            return 0

        for idx, val in enumerate(nums):
            if not idx:
                if isPeak(start, val, nums[idx+1]):
                    return idx
            if idx == len(nums) - 1:
                if isPeak(nums[idx-1], val, last):
                    return idx
            if isPeak(nums[idx-1], val, nums[idx+1]):
                return idx
        