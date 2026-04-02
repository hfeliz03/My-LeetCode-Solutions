from collections import deque 
class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
    
        NEG_INF = float('-inf')
        dp = [[[NEG_INF] * 3 for _ in range(n)] for _ in range(m)]
        
        # base case
        for k in range(3):
            if coins[m-1][n-1] >= 0:
                dp[m-1][n-1][k] = coins[m-1][n-1]
            else:
                # o pagas el costo, o lo neutralizas si puedes
                dp[m-1][n-1][k] = coins[m-1][n-1]
                if k > 0:
                    dp[m-1][n-1][k] = max(dp[m-1][n-1][k], 0)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                    
                for k in range(3):
                    best_next = NEG_INF
                    
                    if i + 1 < m:
                        best_next = max(best_next, dp[i+1][j][k])
                    if j + 1 < n:
                        best_next = max(best_next, dp[i][j+1][k])
                    
                    # no neutralize
                    dp[i][j][k] = best_next + coins[i][j]
                    
                    # neutralize current robber if negative and available
                    if coins[i][j] < 0 and k > 0:
                        best_next_neutral = NEG_INF
                        if i + 1 < m:
                            best_next_neutral = max(best_next_neutral, dp[i+1][j][k-1])
                        if j + 1 < n:
                            best_next_neutral = max(best_next_neutral, dp[i][j+1][k-1])
                        
                        dp[i][j][k] = max(dp[i][j][k], best_next_neutral)
        
        return max(dp[0][0])