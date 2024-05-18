class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ## Detect Cycle in a Directed Graph
        adjList = [[] for _ in range(numCourses)]
        visited = set()
        current_path = set()
        self.ans = []

        for course, preReq in prerequisites:
            adjList[course].append(preReq)

        for course in range(numCourses):
            if not self.dfs(course, adjList, visited, current_path, self.ans):
                return []
        return self.ans

    def dfs(self, course, adjList, visited, current_path, ans):
        if course in current_path:
            return False
        
        if course in visited:
            return True
        
        current_path.add(course)
        neighbors = adjList[course]

        for neighbor in neighbors:
            if not self.dfs(neighbor, adjList, visited, current_path, ans):
                return False
        
        visited.add(course)
        current_path.remove(course)
        ans.append(course)
        return True
            