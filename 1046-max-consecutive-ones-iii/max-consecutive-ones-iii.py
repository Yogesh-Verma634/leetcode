class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = max_ones = 0
        max_allowed = k

        for right, num in enumerate(nums):
            k -= 1 - num

            if k < 0:
                k += 1 - nums[left]
                left += 1
            else:
                max_ones = max(max_ones, right - left + 1)

        return max_ones




            

        