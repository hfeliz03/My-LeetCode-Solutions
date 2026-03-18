class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        # 7 9 18
        # 8 15 24
        # 10 23 38
        #

        if not grid or grid[0][0] > k: return 0
        res = 0
        i = 0
        jLimit = len(grid[0])
        while i < len(grid):
            j = 0 
            while j < len(grid[0]) and j < jLimit:
                if i == 0 and j == 0:
                    pass
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j] 
                else:
                    grid[i][j] += grid[i][j-1] + grid[i-1][j] - grid[i-1][j-1]
                if grid[i][j] <= k: res += 1
                else: jLimit = j
                j+=1
            i+=1
        
        
        
        return res