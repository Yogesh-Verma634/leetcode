class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adjList = {c: set() for word in words for c in word}
        idx_chars = defaultdict(list)

        self.alien_order = []
        
        for curr_w, next_w in zip(words, words[1:]):
            comp_len = min(len(curr_w), len(next_w))
            if len(curr_w) > len(next_w) and curr_w[:comp_len] == next_w[:comp_len]:
                return ""
            for idx in range(comp_len):
                if curr_w[idx] != next_w[idx]:
                    adjList[next_w[idx]].add(curr_w[idx])
                    break

        visited = set()
        path = set()

        def dfs(c):
            visited.add(c)
            path.add(c)
            for neigh in adjList[c]: 
                if neigh not in visited:
                    if not dfs(neigh):
                        return False
                if neigh in path: 
                    return False
                
            self.alien_order.append(c)
            path.remove(c)
            return True

        for c in adjList.keys():
            if c not in visited:
                if not dfs(c):
                    return ""
        
        return ''.join(self.alien_order)
