class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        # left = right = 0
        min_count = flipped = res = 0
        fp = [0]*len(nums)
        for left, num in enumerate(nums):
            if left >= 0:
                flipped ^= fp[left - k]
            if flipped == nums[left]:
                if left + k > len(nums):
                    return -1
                fp[left] = 1
                flipped ^= 1
                res += 1
        
        return res