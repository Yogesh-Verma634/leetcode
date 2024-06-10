class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        ROWS, COLS = len(board), len(board[0])
        
        def dfs_helper(r, c):
            
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != 'O':
                return
            
            board[r][c] = "B"

            directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs_helper(nr, nc)

        for r in range(ROWS):
            if board[r][0] == "O":
                dfs_helper(r, 0) # Boundary spots
            if board[r][COLS-1] == "O":
                dfs_helper(r, COLS-1)

        for c in range(COLS):
            if board[0][c] == "O":
                dfs_helper(0, c) # Boundary spots
            if board[ROWS-1][c] == "O":
                dfs_helper(ROWS-1, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "B":
                    board[r][c] = "O"
