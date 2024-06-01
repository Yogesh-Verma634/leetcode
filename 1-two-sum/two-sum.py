class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(enumerate(nums), key = lambda i: i[1])

        l, r = 0, len(nums)-1

        while l < r:
            curr_sum = nums[l][1] + nums[r][1]

            if curr_sum == target:
                return [nums[l][0], nums[r][0]]
            
            if curr_sum > target:
                r -= 1
            else:
                l += 1

        