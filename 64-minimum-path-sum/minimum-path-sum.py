class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mtx = [[-1 for _ in range(n)] for _ in range(m)]
        mtx[-1][-1] = grid[-1][-1]
        
        for col in range(n-2, -1, -1):
            mtx[-1][col] = mtx[-1][col+1] + grid[-1][col]
        for row in range(m-2, -1, -1):
            mtx[row][-1] = mtx[row+1][-1] + grid[row][-1]
        
        for i in range(m-2, -1, -1):
            for j in range(n-2,-1,-1):
                mtx[i][j] = grid[i][j] + min(mtx[i+1][j], mtx[i][j+1])

        print(mtx)
        return mtx[0][0]