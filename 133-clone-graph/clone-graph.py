"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.clonedGraph = {}
        ### DFS Implementation, TC - O(N), SC - O(N)
        def dfs(curr_node):
            if not curr_node:
                return curr_node

            copy_node = Node(curr_node.val)
            self.clonedGraph[curr_node] = copy_node

            for neigh in curr_node.neighbors:
                if neigh not in self.clonedGraph:
                    copy_node.neighbors.append(dfs(neigh))
                else:
                    copy_node.neighbors.append(self.clonedGraph[neigh])
            
            return copy_node

        return dfs(node)

        ### BFS Implementation, TC - O(N), SC - O(N)
        # if not node:
        #     return node

        # q = collections.deque([node])
        # self.clonedGraph[node] = Node(node.val)

        # while q:
        #     last_node = q.popleft()
        #     for neigh in last_node.neighbors:
        #         if neigh not in self.clonedGraph:
        #             self.clonedGraph[neigh] = Node(neigh.val)
        #             q.append(neigh)
            
        #         self.clonedGraph[last_node].neighbors.append(self.clonedGraph[neigh])

        # return self.clonedGraph[node]