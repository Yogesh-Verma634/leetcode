# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum_ = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        
        # Recursion on Right Subtree
        self.bstToGst(root.right)
        self.sum_ += root.val

        ## Node value update
        root.val = self.sum_

        ## Recursion on Left Subtree
        self.bstToGst(root.left)

        return root
        