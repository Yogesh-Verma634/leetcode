class Solution:

    
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        ### Dijskstra's
        min_heap = []
        heapq.heapify(min_heap)

        ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
        if grid[0][0] == 1 or grid[ROWS][COLS] == 1:
            return -1
        
        dist_matrix = [[float('inf') for _ in range(COLS+1)] for _ in range(ROWS+1)]
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1),(-1, 1),(1, -1)]
        
        min_heap.append([1, (0, 0)])
        grid[0][0] = 1

        while min_heap:

            dist, (r, c) = heapq.heappop(min_heap)
            dist_matrix[r][c] = min(dist_matrix[r][c], dist)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr <= ROWS and 0 <= nc <= COLS and grid[nr][nc] == 0:
                    grid[nr][nc] = 1
                    heapq.heappush(min_heap, [dist+1, (nr, nc)])

        shortest_dist = dist_matrix[ROWS][COLS]
        return  shortest_dist if shortest_dist != float('inf') else -1

        ### BFS Solution
        # ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
        # directions = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1),(-1, 1),(1, -1)]
        # if grid[0][0] == 1 or grid[ROWS][COLS] == 1:
        #     return -1
        
        # q = deque()
        # q.append((0, 0))
        # seen = {(0, 0)}
        
        # curr_dist = 1

        # while q:
        #     print(q)
        #     for _ in range(len(q)):
        #         r, c = q.popleft()

        #         if r == ROWS and c == COLS:
        #             return curr_dist
                
        #         for dr, dc in directions:
        #             nr, nc = r + dr, c + dc
                
        #             if 0 <= nr <= ROWS and \
        #             0 <= nc <= COLS and \
        #             grid[nr][nc] == 0 and \
        #             (nr, nc) not in seen:
        #                 seen.add((nr, nc))
        #                 q.append((nr, nc))

        #     curr_dist += 1

        # return -1


    ## DFS Solution - TLE
        # self.min_path = float('inf')
        # ROWS, COLS = len(grid) - 1, len(grid[0]) - 1
        # seen = {(0, 0)}

        # if grid[0][0] == 1 or grid[ROWS][COLS] == 1:
        #     return -1
        
        # def dfs(x, y, curr_len):
            
        #     if (x, y) == (ROWS, COLS):
        #         self.min_path = min(self.min_path, curr_len)
            
        #     directions = [(1, 1), (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1),(1, -1)]

        #     for dr, dc in directions:
        #         nr, nc = x + dr, y + dc
                
        #         if 0 <= nr <= ROWS and 0 <= nc <= COLS and grid[nr][nc] == 0 and (nr, nc) not in seen \
        #             and curr_len+1 < self.min_path:
        #             seen.add((nr, nc))
        #             dfs(nr, nc, curr_len+1)
                    
        #             seen.remove((nr, nc))
                        
        # dfs(x=0, y=0, curr_len=1)
        # return self.min_path if self.min_path != float('inf') else -1