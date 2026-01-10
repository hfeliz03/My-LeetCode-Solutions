class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)

        # dp[j] will represent dp[i][j] for current i
        dp = [0] * (n + 1)

        # base: dp[m][j] = sum(ord(s2[j:]))
        for j in range(n - 1, -1, -1):
            dp[j] = dp[j + 1] + ord(s2[j])

        # fill from bottom row up
        for i in range(m - 1, -1, -1):
            prev_diag = dp[n]          # dp[i+1][n]
            dp[n] += ord(s1[i])        # dp[i][n] = ord(s1[i]) + dp[i+1][n]

            for j in range(n - 1, -1, -1):
                temp = dp[j]           # dp[i+1][j] (before overwrite)

                if s1[i] == s2[j]:
                    dp[j] = prev_diag
                else:
                    dp[j] = min(
                        ord(s1[i]) + dp[j],      # delete s1[i]
                        ord(s2[j]) + dp[j + 1]   # delete s2[j]
                    )

                prev_diag = temp        # move diag for next j

        return dp[0]