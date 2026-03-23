class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])
        #At every step, store the possibilities and take the one thats best
        #The number of negative cells cannot be odd at the end.
        #  8 -16 1
        #. 8   8 1
        #.-12 -4 1

        # (-16, 8 ) (-16,4) (1,1)
        #.(-12, 8 ) (-2, 8) (1,1)
        #.(-12,-12) (-4,-4) (1,1) 

        dp = [[[] for _ in range(n)] for _ in range(m)]
        dp[-1][-1] = [grid[-1][-1],grid[-1][-1]]
        for i in range(m-2, -1, -1):
            dp[i][-1] = [grid[i][-1]* dp[i+1][-1][0], grid[i][-1]* dp[i+1][-1][1]]
        for j in range(n-2, -1, -1):
            dp[-1][j] = [grid[-1][j]* dp[-1][j+1][0], grid[-1][j]* dp[-1][j+1][1]]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                val = grid[i][j]
                res = [val*dp[i+1][j][0], val*dp[i+1][j][1], val*dp[i][j+1][0], val*dp[i][j+1][1]]
                dp[i][j] = [min(res), max(res)]


        return max(dp[0][0][0], dp[0][0][1]) % MOD if (dp[0][0][0] >= 0 or dp[0][0][1] >= 0) else -1
