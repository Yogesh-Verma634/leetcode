class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        prefix_sum_count_map = collections.defaultdict(int)
        prefix_sum_count_map[0] = 1
        subarray_equal_k_count = 0
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in prefix_sum_count_map:
                subarray_equal_k_count += prefix_sum_count_map[prefix_sum - k]
            
            prefix_sum_count_map[prefix_sum] += 1

        
        return subarray_equal_k_count






        