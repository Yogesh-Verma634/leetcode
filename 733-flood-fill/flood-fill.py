class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        directions = [(0, 0), (0, -1), (0, 1), (1, 0), (-1, 0)]
        ROWS = len(image)
        COLS = len(image[0])
        visited = set()

        color_req = image[sr][sc]

        def dfs_helper(r, c):

            if (r, c) in visited:
                return

            # image[r][c] = color
            # visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and image[nr][nc] == color_req \
                    and (nr, nc) not in visited:
                    image[r][c] = color
                    visited.add((r, c))
                    dfs_helper(nr, nc)

        dfs_helper(sr, sc)
        return image
                 
        