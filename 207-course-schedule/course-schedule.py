class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        ## Detect Cycle in a Directed Graph
        adjList = [[] for _ in range(numCourses)]
        visited = [False for _ in range(numCourses)]
        recS = [False for _ in range(numCourses)]

        for preReq, course in prerequisites:
            adjList[course].append(preReq)

        for course in range(numCourses):
            if not visited[course]:
                if self.dfs(course, adjList, visited, recS):
                    return False
    
        return True

    def dfs(self, course, adjList, visited, recS):
        visited[course] = True
        recS[course] = True

        neighbors = adjList[course]

        for neighbor in neighbors:
            if not visited[neighbor]:
                if (self.dfs(neighbor, adjList, visited, recS)):
                    return True
            elif recS[neighbor]:
                return True
        
        recS[course] = False
        return False

