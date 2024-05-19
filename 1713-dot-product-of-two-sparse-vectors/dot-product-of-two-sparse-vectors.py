class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {}

        for idx, num in enumerate(nums):
            if num:
                self.nums[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        for k in self.nums.keys():
            if k in vec.nums:
                dot_product += self.nums[k] * vec.nums[k]
        return dot_product
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)