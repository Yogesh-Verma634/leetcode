class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        if not mat:
            return mat
        
        ROWS = len(mat)
        COLS = len(mat[0])
        sum = mat[:][:]

        for r in range(ROWS):
            for c in range(COLS):
                sum[r][c] += (sum[r][c-1] if c > 0 else 0) \
                            + (sum[r-1][c] if r > 0 else 0) \
                            - (sum[r-1][c-1] if r > 0 and c > 0 else 0)
        output = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                r1, c1 = max(r - k, 0), max(c - k, 0)
                r2, c2 = min(r + k, ROWS - 1), min(c + k, COLS - 1) 
                output[r][c] = sum[r2][c2] + \
                (sum[r - k - 1][c - k - 1] if (r - k) > 0 and (c - k) > 0 else 0) - \
                (sum[r - k - 1][c2] if (r - k) > 0 else 0) - \
                (sum[r2][c - k - 1] if (c - k) > 0 else 0)
        
        return output
                
        