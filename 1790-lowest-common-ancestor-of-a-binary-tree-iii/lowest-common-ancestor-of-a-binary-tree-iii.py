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
        
        if p == q:
            return True

        if not p or not q:
            return None
        
        path = list()

        while p:
            path.append(p)
            p = p.parent
        
        while q:
            if q in path:
                return q
            q = q.parent
        
        # return  or  or self.lowestCommonAncestor(p.parent, q.parent)

