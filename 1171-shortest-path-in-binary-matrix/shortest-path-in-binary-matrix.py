class Solution:
    from collections import deque

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #init constants
        A = grid
        dirns = [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [-1, 1], [1, -1], [1, 1]] # U, D, L, R, UL, UR, DL, DR
        n = len(A)

        #edge case
        if (A[0][0] == 1) or (A[n-1][n-1] == 1):
            return -1

        #setting base distance for n-1,n-1
        A[n-1][n-1] = 1

        #init queue
        queue = deque()
        if self.isBound(A, n - 1, n - 2) and A[n - 1][n - 2] == 0:
            queue.append([n-1, n-2])
        if self.isBound(A, n - 2, n - 1) and A[n - 2][n - 1] == 0:
            queue.append([n - 2, n - 1])
        if self.isBound(A, n - 2, n - 2) and A[n - 2][n - 2] == 0:
            queue.append([n - 2, n - 2])

        while len(queue):
            #get current node and it's min dist + append neigbours unvisited
            curNode = queue.popleft()
            r = curNode[0]
            c = curNode[1]
            minDist = float('inf')

            #iterate over all 8 neighbors
            for dirn in dirns:
                nr = r + dirn[0]
                nc = c + dirn[1]
                
                #edge case
                if nr == n-1 and nc == n-1:
                    minDist = A[nr][nc]
                
                #normal case
                elif self.isBound(A, nr, nc): #if within bounds
                    if A[nr][nc] == 0: #unvisited node
                        A[nr][nc] = -1
                        queue.append([nr, nc])
                    elif A[nr][nc] != 1 and A[nr][nc] != -1: #visited node, excluding those currently in queue 
                        minDist = min(minDist, A[nr][nc])
            A[r][c] = minDist + 1

        
        return A[0][0] if A[0][0] != 0 else -1
        


    def isBound(self, A, i, j):
        n = len(A)
        return i >= 0 and i < n and j >= 0 and j < n

        
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