# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.min_node = root.val


        def tree_traversal(node, min_val):
            if not node:
                return min_val
            
            diff = abs(node.val - target)

            if diff < min_val:
                self.min_node = node.val
                min_val = diff
            
            if diff == min_val:
                self.min_node = min(node.val, self.min_node)

            if node.left:
                tree_traversal(node.left, min_val)

            if node.right:
                tree_traversal(node.right, min_val)

        tree_traversal(root, abs(target - root.val))
        return self.min_node