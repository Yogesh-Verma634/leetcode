class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        res = []
        if not nums:
            return [[lower, upper]]
        
        prev = lower

        for idx, num in enumerate(nums):
            if prev != num:
                res.append([prev, num-1])

            prev = num + 1

        if num != upper:
            res.append([num+1, upper])
        return res

        