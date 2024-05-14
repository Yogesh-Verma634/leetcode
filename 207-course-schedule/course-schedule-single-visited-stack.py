class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool: 
        ## Detect Cycle in a Directed Graph

        # Adjcency list of course and preReqs
        prereqMap = {course: [] for course in range(numCourses)}
        for course, preReq in prerequisites:
            prereqMap[course].append(preReq)

        # stores courses in the current DFS path
        visitSet = set()

        # DFS call return if it is possible to take a course or not
        def dfs(course) -> bool:
            if course in visitSet:
                return False
            if not prereqMap[course]:
                return True
            visitSet.add(course)

            for preReq in prereqMap[course]:
                course_possible = dfs(preReq)
                if not course_possible:
                    return False
            visitSet.remove(course)
            prereqMap[course] = []
            return True

        for course in range(numCourses):
            course_possible = dfs(course)
            if not course_possible:
                return False
        return True
