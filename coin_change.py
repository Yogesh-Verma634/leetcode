'''
322. Coin Change

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

-------------------------------------
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        
        for am in range(1, amount+1):
            for c in coins:
                
                if am - c >= 0:
                    dp[am] = min(dp[am], 1 + dp[am - c])
        
        print(dp)
        out = dp[amount]
        return out if out != (amount+1) else -1
