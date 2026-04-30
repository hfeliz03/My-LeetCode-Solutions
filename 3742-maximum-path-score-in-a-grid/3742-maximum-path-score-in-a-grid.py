class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        #How is this not a hard bruh
        rows, cols = len(grid), len(grid[0])

        # dp[i][j][c] = max score starting at (i,j) using exactly c cost
        dp = [[[-10**9] * (k + 1) for _ in range(cols)] for _ in range(rows)]
        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                val = grid[i][j]
                if val == 1:
                    score, cost = 1, 1
                elif val == 2:
                    score, cost = 2, 1
                else:
                    score, cost = 0, 0
                for c in range(cost, k + 1):
                    if i == rows - 1 and j == cols - 1:
                        dp[i][j][c] = score
                    else:
                        best_next = -10**9
                        if i + 1 < rows:
                            best_next = max(best_next, dp[i + 1][j][c - cost])
                        if j + 1 < cols:
                            best_next = max(best_next, dp[i][j + 1][c - cost])
                        if best_next != -10**9:
                            dp[i][j][c] = score + best_next
        ans = max(dp[0][0])
        return ans if ans >= 0 else -1