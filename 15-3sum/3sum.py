class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)
        triplets = set()

        ## [-1,0,1,2,-1,-4]
        # seen = {0}
        # x_idx -> 0, y_idx -> 1
        # X -> -1
        # Y -> 1
        # Z -> 0

        # X + Y + Z = 0
        for x_idx in range(len(nums)-1):
            if x_idx > 0 and nums[x_idx] == nums[x_idx - 1]:
                continue
            X = nums[x_idx]
            
            y_idx = x_idx + 1
            z_idx = len(nums) - 1

            while y_idx < z_idx:
                Y = nums[y_idx]
                Z = nums[z_idx]

                curr_sum = X + Y + Z

                if curr_sum == 0:
                    triplets.add((X, Y, Z))
                if curr_sum > 0:
                    z_idx -= 1
                else:
                    y_idx += 1
                
                
        
        return triplets