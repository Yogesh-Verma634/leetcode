class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ROWS, COLS = len(mat), len(mat[0])
        res = []
        top = False
        for c in range(COLS):
            diag = []
            r = 0
            while 0 <= r < ROWS and 0 <=  c < COLS:
                diag.append(mat[r][c])
                c -= 1
                r += 1
            
            if top:
                top = False
            else:
                diag = diag[::-1]
                top = True
            res.extend(diag)
        

        for r in range(1, ROWS):
            c = COLS-1
            diag = []
            while 0 <=  r < ROWS and 0 <= c < COLS:
                diag.append(mat[r][c])
                c -= 1
                r += 1
            if top:
                top = False
            else:
                diag = diag[::-1]
                top = True
            res.extend(diag)
        return res

        