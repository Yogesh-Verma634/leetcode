class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        
        if not mat:
            return mat
        
        ROWS = len(mat)
        COLS = len(mat[0])
        sum = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]
        for r in range(ROWS):
            for c in range(COLS):
                sum[r+1][c+1] = mat[r][c]

        for r in range(ROWS):
            for c in range(COLS):
                sum[r+1][c+1] += (sum[r+1][c]) \
                            + (sum[r][c+1]) \
                            - (sum[r][c])
        output = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        # print(sum)
        for r in range(ROWS):
            for c in range(COLS):
                r1, c1 = max(r - k, 0), max(c - k, 0)
                r2, c2 = min(r + k + 1, ROWS), min(c + k + 1, COLS)
                output[r][c] = sum[r2][c2] + sum[r1][c1] - sum[r2][c1] - sum[r1][c2]
        
        return output
                
        