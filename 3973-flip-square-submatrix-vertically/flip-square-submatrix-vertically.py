class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        #x and y is top left corner of square submatrix and the int k size of the submatrix
        #submatrix is squared
        m = len(grid)
        n = len(grid[0])
        kSubmatrix = []

        i, j = x, y
        for subRow in grid[x:x+k]:
            kSubmatrix.append(subRow[y:y+k]) 

        for i in range(m):
            if i == x:
                grid[i][y:y+k] = kSubmatrix.pop()
                if kSubmatrix: x+=1
        
        return grid