class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]

        for idx in range(1, len(nums)):
            num = nums[idx]
            # 1. Split: dp[i-1] - num
            # 2. Not Split: dp[i-2] - dp[i-1] + num
            dp[idx+1] = max(dp[idx]+num, dp[idx-1]+nums[idx-1]-num)
            # print(dp[idx+1])


        return dp[len(nums)]
