class SegmentTree:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.count = 1
        self.val = val
        
class Solution:
    
    def insertNode(self, root, val):
        node = SegmentTree(val)
        curr_node_count = 0

        while root:
            if val <= root.val:
                root.count += 1
                
                if not root.left:
                    root.left = node
                    break
                else:
                    root = root.left
                
            else:
                curr_node_count += root.count
                if not root.right:
                    root.right = node
                    break
                else:
                    root = root.right
        return curr_node_count

    #nums: List[int] 
    def countSmaller(self, nums):
        
        output = [0]*len(nums)
        if not nums:
            return []
        
        root = SegmentTree(nums[len(nums)-1])
        
        for idx in range(len(nums)-2, -1, -1):
            count = self.insertNode(root, nums[idx])
            output[idx] = count
            
        return output

solution = Solution()
input = [5,2,6,0,1]
print(solution.countSmaller(input))
            