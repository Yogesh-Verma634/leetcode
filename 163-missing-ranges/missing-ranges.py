class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if not nums:
            return [[lower, upper]]
        for idx, num in enumerate(nums):

            if idx == 0:
                left = lower
            else:
                left = nums[idx-1]+1
            right = num
            
            if left != right:
                res.append([left, right-1])

            if idx == len(nums)-1:
                left = num
                right = upper
                if left != right:
                    res.append([left+1, right])

        return res

        