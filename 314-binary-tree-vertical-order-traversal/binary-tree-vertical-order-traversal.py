# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        ## Iterative BFS
        if not root:
            return []
        q = deque([(root, 0)])
        mapping = defaultdict(list)
        # hd -> Horizontal distance from root node
        while q:
            node, hd = q.popleft()
            mapping[hd].append(node.val)

            if node.left:
                q.append([node.left, hd - 1])
            if node.right:
                q.append([node.right, hd + 1])

        return [mapping[hd] for hd in range(min(mapping), max(mapping)+1)]
    
        ### Recursive DFS
        # self.traversal_map = {}
        # self.order = []

        # def dfs(node, horizontal_level, vertical_level):
        #     if not node:
        #         return
        #     if horizontal_level not in self.traversal_map:
        #         self.traversal_map[horizontal_level] = []
        #     self.traversal_map[horizontal_level].append((vertical_level, node.val)) 

        #     dfs(node.left, horizontal_level - 1, vertical_level + 1)
        #     dfs(node.right, horizontal_level + 1, vertical_level + 1)

        # dfs(root, 0, 0)
        # for level in sorted(self.traversal_map.keys()):
        #     print(level)
        #     self.traversal_map[level].sort(key=lambda a: a[0])
        #     self.order.append([item[1] for item in self.traversal_map[level]])
        # return self.order

