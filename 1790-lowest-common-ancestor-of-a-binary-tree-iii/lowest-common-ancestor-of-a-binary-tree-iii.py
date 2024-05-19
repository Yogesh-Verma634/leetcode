"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        
        # Slow and Fast pointer types traversal
        p_copy = p
        q_copy = q

        while p_copy != q_copy:
            if not p_copy:
                p_copy = q
            else:
                p_copy = p_copy.parent

            if not q_copy:
                q_copy = p
            else:
                q_copy = q_copy.parent
        
        return p_copy



        ### Path Traversal
        ### SC - O(2N), TC - O(N*N) where N is the depth of tree
        # path = list()
        # while p:
        #     path.append(p)
        #     p = p.parent
        
        # while q:
        #     if q in path:
        #         return q
        #     q = q.parent
