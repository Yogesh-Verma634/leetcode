class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        total_sum = int(len(nums) * (len(nums) + 1) / 2)

        arr_sum = sum(nums)

        return total_sum - arr_sum
        