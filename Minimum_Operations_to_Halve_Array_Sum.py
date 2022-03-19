'''
2208. Minimum Operations to Halve Array Sum

You are given an array nums of positive integers. In one operation, you can choose any number from nums and reduce it to exactly half the number. (Note that you may choose this reduced number in future operations.)
Return the minimum number of operations to reduce the sum of nums by at least half.

Input: nums = [5,19,8,1]
Output: 3

Explanation: The initial sum of nums is equal to 5 + 19 + 8 + 1 = 33.
The following is one of the ways to reduce the sum by at least half:
Pick the number 19 and reduce it to 9.5.
Pick the number 9.5 and reduce it to 4.75.
Pick the number 8 and reduce it to 4.
The final array is [5, 4.75, 4, 1] with a total sum of 5 + 4.75 + 4 + 1 = 14.75. 
The sum of nums has been reduced by 33 - 14.75 = 18.25, which is at least half of the initial sum, 18.25 >= 33/2 = 16.5.
Overall, 3 operations were used so we return 3.
It can be shown that we cannot reduce the sum by at least half in less than 3 operations.
'''

class Solution:
    def halveArray(self, nums: List[int]) -> int:
        
        total = sum(nums)
        heap = [-x for x in nums]
        heapify(heap)
        
        curr_sum = total 
        count = 0
        while (2*curr_sum) > total:
            max_ = heappop(heap) * -1
            curr_sum -= (max_/2.0)
            heappush(heap, -max_/2.0)
            count += 1
        
        '''
        def halveArray(self, nums: List[int]) -> int:
        pool = [1.0 * -x for x in nums]
        heapify(pool)
        total = 1.0 * sum(nums)
        cur = 0.0
        ans = 0
        while pool:
            ans += 1
            cur_max = heappop(pool) * -1
            cur += cur_max / 2.0
            if 2 * cur >= total:
                return ans
            heappush(pool, - cur_max / 2.0)
        return ans
        
        # credits: https://leetcode.com/yeu_nhung/
        '''
        
        
        return count
