# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ### Iterative BFS - Using Stack
        if not root:
            return 0
        level_stack = [[root, 1]]
        max_depth = 0

        while level_stack:
            node, depth = level_stack.pop()
            max_depth = max(max_depth, depth)
            if node.left:
                level_stack.append([node.left, depth+1])
            if node.right:
                level_stack.append([node.right, depth+1])

        return max_depth

        ### Iterative DFS - Using Queue
        # if not root:
        #     return 0
        # level = 0
        # level_q = deque([root])
        # while level_q:
        #     for i in range(len(level_q)):
        #         node = level_q.popleft()
        #         if node.left:
        #             level_q.append(node.left)
        #         if node.right:
        #             level_q.append(node.right)
        #     level += 1
        # return level


        ### Recursive DFS
        # if not root:
        #     return 0
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        