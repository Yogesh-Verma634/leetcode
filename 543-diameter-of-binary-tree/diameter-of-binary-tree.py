# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        
        def diameterOfBinaryTreeUtil(root):
            if not root:
                return 0
            
            left_h = diameterOfBinaryTreeUtil(root.left)
            right_h = diameterOfBinaryTreeUtil(root.right)
            res[0] = max(res[0], left_h + right_h)
            return 1 + max(left_h, right_h)

        diameterOfBinaryTreeUtil(root)
        return res[0]