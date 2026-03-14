class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #In place,
        #Track the row and cols index at where you observe the zeroes
        #then start making the changes
        zeroRows = set()
        zeroCols = set()
        for i, row in enumerate(matrix):
            for j, element in enumerate(row):
                if element == 0: 
                    zeroRows.add(i)
                    zeroCols.add(j)

        for i, row in enumerate(matrix):
            j = 0
            while j < len(row):
                if i in zeroRows or j in zeroCols:
                    matrix[i][j] = 0
                j+=1
        
