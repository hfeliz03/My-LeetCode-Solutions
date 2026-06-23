class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10 ** 9 + 7
        r -= l
        dp = [[0] * (r + 1) for _ in range(n)]
        for j in range(r + 1): dp[0][j] = 1

        for i in range(1, n):
            prev = 0
            if i % 2 == 1:
                for j in range(r + 1):
                    dp[i][j] = prev
                    prev = (prev + dp[i - 1][j]) % MOD
            else:
                for j in range(r, -1, -1):
                    dp[i][j] = prev
                    prev = (prev + dp[i - 1][j]) % MOD
        
        return (sum(dp[-1]) * 2) % MOD