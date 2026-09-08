class NumMatrix:
    sumMtx = [[]]
    rows = 0
    cols = 0
    def __init__(self, matrix: List[List[int]]):
        self.rows = len(matrix)
        self.cols = len(matrix[0])
        self.sumMtx = [[0 for _ in range(self.cols)] for _ in range(self.rows)] 
        for i in range(self.rows-1,-1,-1):
            for j in range(self.cols-1, -1, -1):
                self.sumMtx[i][j] += matrix[i][j]
                if i + 1 < self.rows:
                    self.sumMtx[i][j] += self.sumMtx[i+1][j]
                if j + 1 < self.cols:  
                    self.sumMtx[i][j] += self.sumMtx[i][j+1]
                if i + 1 < self.rows and j + 1 < self.cols:
                    self.sumMtx[i][j] -= self.sumMtx[i+1][j+1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row2 >= self.rows-1 and col2 >= self.cols-1: return self.sumMtx[row1][col1]
        elif row2 >= self.rows-1: return self.sumMtx[row1][col1] - self.sumMtx[row1][col2+1]
        elif col2 >= self.cols-1: return self.sumMtx[row1][col1] - self.sumMtx[row2+1][col1]
        else:
            return self.sumMtx[row1][col1] - self.sumMtx[row1][col2+1] - self.sumMtx[row2+1][col1] + self.sumMtx[row2+1][col2+1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)