# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.vert_map = defaultdict(list)
        ### DFS Implementation
        def dfs(node, hd, vd):
            if not node:
                return
            self.vert_map[hd].append((node.val, vd))
            dfs(node.left, hd - 1, vd + 1)
            dfs(node.right, hd + 1, vd + 1)
        dfs(root, 0, 0)

        vertical_order = []
        for key, val in sorted(self.vert_map.items()):
            val.sort(key = lambda a: (a[1], a[0]))
            vertical_order.append(v for v, d in val)
        return vertical_order

        ### BFS implementation, TC - O(N) for queue, O(N Log N) for worst sorting 
        # SC - O(N) for deque, O(width) -> O(N) for worst
        # q = collections.deque([(root, 0, 0)]) # (node, horizontal_distance, vertical_depth)
        # vert_map = defaultdict(list) ## index is horizontal distance 
        # while q:
        #     node, hd, vd = q.popleft()
        #     ## Store both vertical depth and node value in the map 
        #     vert_map[hd].append((node.val, vd))
        #     if node.left:
        #         q.append((node.left, hd - 1, vd + 1))
        #     if node.right:
        #         q.append((node.right, hd + 1, vd + 1))

        # vertical_order = []
        
        # # Sort the map first by the vertical distance and then by value
        # for key, val in sorted(vert_map.items()):
        #     val.sort(key = lambda a: (a[1], a[0]))
        #     vertical_order.append(v for v, d in val)
        # return vertical_order


        