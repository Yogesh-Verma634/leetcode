# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:

        self.arr = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.arr.append(node.val)
            dfs(node.right)
        
        l,r = 0, len(self.arr)-1
        
        def createBST(l, r):
            mid = (l + r)//2

            if l > r:
                return None

            if mid >= len(self.arr) or mid < 0:
                return None
            node = TreeNode(self.arr[mid])

            node.left = createBST(l, mid-1)
            node.right = createBST(mid+1, r)
            return node

        dfs(root)
        return createBST(0, len(self.arr)-1)
            

            


        