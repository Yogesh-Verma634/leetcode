# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.traversal_map = {}
        self.order = []

        def dfs(node, horizontal_level, vertical_level):
            if not node:
                return
            if horizontal_level not in self.traversal_map:
                self.traversal_map[horizontal_level] = []
            self.traversal_map[horizontal_level].append([vertical_level, node.val]) 

            dfs(node.left, horizontal_level - 1, vertical_level + 1)
            dfs(node.right, horizontal_level + 1, vertical_level + 1)

        dfs(root, 0, 0)
        # print(self.traversal_map)
        levels = [v for k, v in sorted(self.traversal_map.items())]
        # print(levels)
        for level in levels:
            level.sort(key=lambda a: a[0])
            self.order.append([l[1] for l in level])
        return self.order

