class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #In place,
        #Track the row and cols index at where you observe the zeroes
        #then start making the changes
        # zeros = set()
        # for i, row in enumerate(matrix):
        #     for j, element in enumerate(row):
        #         if element == 0: 
        #             zeros.add(i)
        #             zeros.add(j)

        # for i, row in enumerate(matrix):
        #     j = 0
        #     while j < len(row):
        #         if i in zeros or j in zeros:
        #             matrix[i][j] = 0
        #         j+=1

        #Forced way to do O(1) space
        ROWS, COLS = len(matrix), len(matrix[0])
        rowZero = False

        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r > 0: 
                        matrix[r][0] = 0
                    else: 
                        rowZero = True
        
        for r in range(1,ROWS):
            for c in range(1,COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0
                
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
        
        if rowZero: 
            for c in range(COLS):
                matrix[0][c] = 0

        
