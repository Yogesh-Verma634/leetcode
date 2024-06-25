class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:

        apples = sum(bool(app) for app in hasApple)

        self.collected = 0
        node = 0
        visited = set()
        inrecursion = set()
        self.count = 0

        self.adjList = defaultdict(list)

        for src, dest in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)

        def dfs(node):
            visited.add(node)
            time = 0

            for child in self.adjList[node]:
                if child not in visited:
                    child_time = dfs(child)
                    if child_time or hasApple[child]:
                        time += 2 + child_time

            return time

        return dfs(0)

        


        