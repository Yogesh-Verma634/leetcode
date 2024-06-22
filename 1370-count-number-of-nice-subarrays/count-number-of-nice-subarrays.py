class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_oddcount = defaultdict(int)
        prefix_oddcount[0] += 1

        odd_count = 0
        ans = 0
        for num in nums:
            if num % 2 != 0:
                odd_count += 1
            if (odd_count - k) in prefix_oddcount:
                ans += prefix_oddcount[odd_count - k]
            
            prefix_oddcount[odd_count] += 1
        
        return ans
            

        