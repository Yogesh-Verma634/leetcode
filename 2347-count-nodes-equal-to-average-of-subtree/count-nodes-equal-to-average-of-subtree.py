# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.num_nodes = 0

        def dfs(node):
            if not node:
                return (0, 0)

            left_sum, left_nodes = dfs(node.left)
            right_sum, right_nodes = dfs(node.right)

            N = 1 + left_nodes + right_nodes
            _sum = node.val + left_sum + right_sum
            avg = _sum // N
            # print(left_sum, right_sum, node.val)
            if avg == node.val:
                self.num_nodes += 1

            return (_sum, N)

        dfs(root)
        return self.num_nodes
        