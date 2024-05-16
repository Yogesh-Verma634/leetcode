# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        sum_leaf_to_node = [0]
        def dfs(node, path):
            if not node:
                return
            
            if not node.left and not node.right:
                sum_leaf_to_node[0] += int(path + str(node.val))
                return
            
            dfs(node.left, path + str(node.val))
            dfs(node.right, path + str(node.val))
        
        
        dfs(root, '')
        return sum_leaf_to_node[0]