class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ## X + Y + Z = 0
        # Y + Z = -X => Z = -X + (-Y)
        nums.sort()
        triplets = set()

        ## [-1,0,1,2,-1,-4]
        # seen = {0}
        # x_idx -> 0, y_idx -> 1
        # X -> -1
        # Y -> 1
        # Z -> 0

        # X + Y + Z = 0
        for x_idx in range(len(nums)-1):
            Variable.X = nums[x_idx]

            if x_idx > 0 and nums[x_idx] == nums[x_idx - 1]:
                continue
            seen = set()

            target_sum = -Variable.X
            for y_idx in range(x_idx+1, len(nums)):
                Variable.Y = nums[y_idx]
                Variable.Z = (target_sum - Variable.Y)
                
                if Variable.Z in seen:
                    triplet = [Variable.X, Variable.Y, Variable.Z]
                    triplets.add(tuple(sorted(triplet)))
                
                seen.add(Variable.Y)
        
        return triplets

class Variable:
    X = 0
    Y = 0
    Z = 0
