# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or root == p or root == q:
            return root
        left_ = self.lowestCommonAncestor(root.left, p, q)
        right_ = self.lowestCommonAncestor(root.right, p, q)

        if left_ and right_:
            return root
        
        if left_ or right_:
            return left_ or right_
        
        return None
        