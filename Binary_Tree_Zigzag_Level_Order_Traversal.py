class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = [root]
        flag = 0
        
        while q:
            temp = []
            print(q)
            for idx in range(len(q)):
                node = q.pop(0)
                temp.append(node.val) 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            
            if flag == 1:
                temp = temp[::-1]
            res.append(temp)
            flag = 1 if flag == 0 else 0
            
        return res
