class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        ### Binary Search Solution, TC - O(log n)
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r - l) // 2)
            if mid < len(nums) - 1 and nums[mid] < nums[mid + 1]:
                l = mid + 1
            elif mid and nums[mid] < nums[mid - 1]:
                r = mid - 1
            else:
                return mid
        

        ### Brute Force Solution, TC - O(N)
        # start = last = float('-inf')
        # def isPeak(prev, curr, next):
        #     return curr > prev and curr > next

        # if len(nums) == 1:
        #     return 0

        # for idx, val in enumerate(nums):
        #     if not idx:
        #         if isPeak(start, val, nums[idx+1]):
        #             return idx
        #     if idx == len(nums) - 1:
        #         if isPeak(nums[idx-1], val, last):
        #             return idx
        #     if isPeak(nums[idx-1], val, nums[idx+1]):
        #         return idx
        

        ### Brute Force Solution, TC - O(N)
        # start = last = float('-inf')
        # def isPeak(prev, curr, next):
        #     return curr > prev and curr > next

        # if len(nums) == 1:
        #     return 0

        # for idx, val in enumerate(nums):
        #     if not idx:
        #         if isPeak(start, val, nums[idx+1]):
        #             return idx
        #     if idx == len(nums) - 1:
        #         if isPeak(nums[idx-1], val, last):
        #             return idx
        #     if isPeak(nums[idx-1], val, nums[idx+1]):
        #         return idx
        