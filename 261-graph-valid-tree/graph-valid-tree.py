class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        ### Union Find solution
        self.parent_arr = [i for i in range(n)]

        def find(node):
            if self.parent_arr[node] == node:
                return node
            self.parent_arr[node] = find(self.parent_arr[node])
            return self.parent_arr[node]

        def union(node1, node2):
            par_node1 = find(node1)
            par_node2 = find(node2)

            if par_node1 == par_node2:
                return False
            self.parent_arr[par_node1] = par_node2
            return True
        
        for edge1, edge2 in edges:
            if not union(edge1, edge2):
                return False
            
        root = find(0)

        for i in range(n):
            if find(i) != root:
                return False
        return True

        ### Detect Cycle using DFS Solution
        # adjList = collections.defaultdict(list)
        # for src, dest in edges:
        #     adjList[src].append(dest)
        #     adjList[dest].append(src)

        # visited = set()
        # def dfs(node, parent):
        #     if node in visited:
        #         return False
            
        #     visited.add(node)
        #     for neighbor in adjList[node]:
        #         if neighbor not in visited:
        #             if not dfs(neighbor, node):
        #                 return False
        #         elif neighbor != parent:
        #                 return False
                    
            
        #     return True
        
        # if not dfs(0, 0):
        #     return False
        # for i in range(n):
        #     if i not in visited:
        #             return False
        # return True
        