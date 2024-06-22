class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ROWS = len(isConnected)
        COLS = len(isConnected[0])
        self.visited = [0] * ROWS

        self.adjList = defaultdict(list)
        for row in range(ROWS):
            for col in range(COLS):
                if isConnected[row][col]:
                    self.adjList[row].append(col)

        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(node):    
            self.visited[node] = 1
            for neigh in self.adjList[node]:
                if not self.visited[neigh]:
                    dfs(neigh)

        connected = 0
        for i in range(ROWS):
            if not self.visited[i]:
                connected += 1
                dfs(i)
        
        return connected