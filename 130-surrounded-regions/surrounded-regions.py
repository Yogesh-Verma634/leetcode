class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        visited = set()

        def dfs_helper(r, c):
            
            if r >= ROWS or c >= COLS:
                return False
            
            if board[r][c] == "X":
                return True

            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    return False
                if board[nr][nc] == "O" and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    if not dfs_helper(nr, nc):
                        return False
            
            # visited = set()
            return True
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    visited = set()
                    if dfs_helper(r, c):
                        board[r][c] = "X"
                        for sr, sc in visited:
                            board[sr][sc] = "X"
                
