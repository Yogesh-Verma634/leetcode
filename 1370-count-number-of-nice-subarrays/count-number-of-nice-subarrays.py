class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        ## Sliding window approach
        left, right = 0, 0
        prev_odd_count = odd_count = result = 0

        while right < len(nums):
            ## Odd
            if nums[right] % 2 != 0:
                odd_count += 1
                prev_odd_count = 0

            while odd_count == k:
                prev_odd_count += 1

                if nums[left] % 2 == 1:
                    odd_count -= 1
                
                left += 1
            result += prev_odd_count
            right += 1
        
        return result




        ### Prefix Array Method
        # prefix_oddcount = defaultdict(int)
        # prefix_oddcount[0] += 1

        # odd_count = 0
        # ans = 0
        # for num in nums:
        #     if num % 2 != 0:
        #         odd_count += 1
        #     if (odd_count - k) in prefix_oddcount:
        #         ans += prefix_oddcount[odd_count - k]
            
        #     prefix_oddcount[odd_count] += 1
        
        # return ans
            

        