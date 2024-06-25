# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.sum_ = 0
        def tree_traversal(node):
            if not node:
                return
            
            # Recursion on Right Subtree
            right_val = tree_traversal(node.right)
            self.sum_ += node.val

            ## Node value update
            node.val = self.sum_

            ## Recursion on Left Subtree
            tree_traversal(node.left)
                
        tree_traversal(root)
        return root
        