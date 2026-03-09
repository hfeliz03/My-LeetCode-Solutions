class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #iterate until we have reached grid[m-1][n-1]
        #If we are following one same direction, dont increase
        #If we can change direction, increase by one more
        #DP table with the count of paths we can take at each [i][j]
        # 28 21 15 10 6 3 1
        # 7 6 5 4 3 2 1
        # 1 1 1 1 1 1 0 
        # Base cases are at the edges, because we will only be able to go either right or down.
        dp = [[0]*n for _ in range(m)]
        for row in dp:
            row[-1] = 1
        for i in range(len(dp[-1])):
            dp[-1][i] = 1

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        print(dp)
        return dp[0][0]