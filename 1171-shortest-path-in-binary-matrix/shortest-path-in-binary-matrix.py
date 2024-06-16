class Solution:

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1),(-1, 1),(1, -1)]
        if grid[0][0] == 1 or grid[ROWS][COLS] == 1:
            return -1
        
        q = deque()
        q.append((0, 0))
        seen = {(0, 0)}
        
        curr_dist = 1

        while q:

            for _ in range(len(q)):
                r, c = q.popleft()

                if r == ROWS and c == COLS:
                    return curr_dist
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                
                    if 0 <= nr <= ROWS and \
                    0 <= nc <= COLS and \
                    grid[nr][nc] == 0 and \
                    (nr, nc) not in seen:
                        seen.add((nr, nc))
                        q.append((nr, nc))

            curr_dist += 1

        return -1


# class Solution:
#     def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
#         self.min_path = float('inf')
#         ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
#         dist = set()

#         if grid[0][0] == 1 or grid[ROWS][COLS] == 1:
#             return -1

#         def dfs(x, y, curr_len):
#             # if curr_len > self.min_path:
#             #     return -1

#             if (x, y) == (ROWS, COLS):
#                 self.min_path = min(self.min_path, curr_len)
            
#             grid[x][y] = 1

#             directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1),(-1, 1),(1, -1)]

#             for dr, dc in directions:
#                 nr, nc = x + dr, y + dc
                
#                 if 0 <= nr <= ROWS and 0 <= nc <= COLS and grid[nr][nc] == 0 and curr_len+1 < self.min_path:
#                     dfs(nr, nc, curr_len+1)
            
#             grid[x][y] = 0
            
#         dfs(x=0, y=0, curr_len=1)
#         return self.min_path if self.min_path != float('inf') else -1