class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        self.adjList = defaultdict(list)

        for src, dest in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)
        
        ## DFS Solution
        visited = set()
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbor in self.adjList[node]:
                    dfs(neighbor)
        count = 0
        for idx in range(n):
            if idx not in visited:
                dfs(idx)
                count += 1
        return count
        
        ### Union Find Solution => TC - O(N log N), SC - O(N) 
        # self.par = {}
        # self.rank = {}

        # for i in range(0, n):
        #     self.par[i] = i
        #     self.rank[i] = 0
        
        # for edge1, edge2 in edges:
        #     self.union(edge1, edge2)
        
        # parent_set = set()
        # for i in range(0, n):
        #     parent = self.find(i)
        #     if parent not in parent_set:
        #         parent_set.add(parent)
        
        # return len(parent_set)
    
    # Find parent of n, with path compression.
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by height / rank.
    # Return false if already connected, true otherwise.
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False
        
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True