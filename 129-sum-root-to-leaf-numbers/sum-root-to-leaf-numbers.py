# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum_leaf_to_node = 0

        def dfs(node, path):
            # If we reach an empty leaf node - Node of a parent with either left or right empty
            if not node:
                return

            ## If we reach the leaf node => calculate sum of this path
            if not node.left and not node.right:
                self.sum_leaf_to_node += int(path + str(node.val))
                return

            ## Recursively call for both left and right sides
            dfs(node.left, path + str(node.val))
            dfs(node.right, path + str(node.val))

        ## Recursively go over all the paths from root to leaf nodes
        dfs(root, "")
        return self.sum_leaf_to_node
