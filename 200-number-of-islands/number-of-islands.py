class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = [(0, 0), (0, -1), (0, 1), (1, 0), (-1, 0)]

        def dfs_helper(r, c):
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited and grid[nr][nc] == "1":
                    visited.add((nr, nc))
                    dfs_helper(nr, nc)
        
        connected_comp = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    connected_comp += 1
                    visited.add((r, c))
                    dfs_helper(r, c)
        
        return connected_comp



        