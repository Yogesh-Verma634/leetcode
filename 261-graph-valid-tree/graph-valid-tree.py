class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = collections.defaultdict(list)
        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    if not dfs(neighbor, node):
                        return False
                elif neighbor != parent:
                        return False
                    
            
            return True
        
        if not dfs(0, 0):
            return False
        for i in range(n):
            if i not in visited:
                    return False
        return True
        