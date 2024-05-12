# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.rangeSumBSTUtil(root, low, high)
    
    def rangeSumBSTUtil(self, node, low, high):
        range_sum = 0
        if not node:
            return 0

        if node.val < low:
            return self.rangeSumBSTUtil(node.right, low, high)
        elif node.val > high:
            return self.rangeSumBSTUtil(node.left, low, high)
        else:
            left_range_sum = self.rangeSumBSTUtil(node.left, low, high)
            right_range_sum = self.rangeSumBSTUtil(node.right, low, high)

            return node.val + left_range_sum + right_range_sum
            
        