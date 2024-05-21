class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        ### Binary Search Solution, TC - O(log n)
        left, mid, right = 0, 0, len(nums)-1       
        while left<right:            
            mid = (left+right)//2
            if nums[mid]>nums[mid+1]:
                right = mid
            else:
                left = mid +1               
        return left

        

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
        