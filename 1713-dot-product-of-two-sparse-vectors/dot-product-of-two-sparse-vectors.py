class SparseVector:
    def __init__(self, nums: List[int]):
        
        ## Tuple Solution
        self.nums = []
        for idx, num in enumerate(nums):
            if num:
                self.nums.append((idx, num))
        
        ## Hashmap solution
        # self.nums = {}
        # for idx, num in enumerate(nums):
        #     if num:
        #         self.nums[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        
        ### Tuple solution
        nums_idx = vec_idx = 0
        while nums_idx < len(self.nums) and vec_idx < len(vec.nums):
            v1_idx = self.nums[nums_idx][0]
            v2_idx = vec.nums[vec_idx][0]

            if v1_idx == v2_idx:
                v1_val = self.nums[nums_idx][1]
                v2_val = vec.nums[vec_idx][1]
                dot_product += v1_val * v2_val
                nums_idx += 1
                vec_idx += 1
            
            elif v1_idx < v2_idx:
                nums_idx += 1
            else:
                vec_idx += 1

        return dot_product
        ### Hashmap solution
        # for k in self.nums.keys():
        #     if k in vec.nums:
        #         dot_product += self.nums[k] * vec.nums[k]
        # return dot_product



# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)