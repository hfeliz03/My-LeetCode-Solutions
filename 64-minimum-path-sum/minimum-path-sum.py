class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for col in range(n-2, -1, -1):
            grid[-1][col] = grid[-1][col+1] + grid[-1][col]
        for row in range(m-2, -1, -1):
            grid[row][-1] = grid[row+1][-1] + grid[row][-1]
        
        for i in range(m-2, -1, -1):
            for j in range(n-2,-1,-1):
                grid[i][j] = grid[i][j] + min(grid[i+1][j], grid[i][j+1])

        return grid[0][0]