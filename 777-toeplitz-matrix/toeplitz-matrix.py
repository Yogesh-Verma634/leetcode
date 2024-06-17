class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        
        for c in range(COLS):
            r = 0
            val = matrix[r][c]
            while r < ROWS and c < COLS:
                if val != matrix[r][c]:
                    return False
                r += 1
                c += 1
        
        
        for r in range(ROWS):
            c = 0
            val = matrix[r][c]
            while r < ROWS and c < COLS:
                if val != matrix[r][c]:
                    return False
                r += 1
                c += 1
        
        return True
        


        