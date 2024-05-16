# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        ## If we reach end of the tree i.e. leaf node's children or we find one of the p or q -> return the current node
        if not root or root == p or root == q:
            return root

        ## Call LCS recursively on left and right
        left_ = self.lowestCommonAncestor(root.left, p, q)
        right_ = self.lowestCommonAncestor(root.right, p, q)

        ## If we find p and q on different sides => current node is lowest common ancestor
        if left_ and right_:
            return root

        ## If we get both p and q on one side, return that side 
        return left_ or right_
        
