class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        # Bruh this is NOT a medium
        # I DID NOT WRITE THIS
        MOD = 10**9 + 7

        dp = [[[0] * 2 for _ in range(one + 1)] for _ in range(zero + 1)]

        for z in range(1, min(limit, zero) + 1): dp[z][0][0] = 1
        for o in range(1, min(limit, one) + 1): dp[0][o][1] = 1

        for z in range(1, zero + 1):
            for o in range(1, one+1):
                dp[z][o][0] = (dp[z-1][o][0] + dp[z-1][o][1]) % MOD
                if z > limit: dp[z][o][0] = (dp[z][o][0] - dp[z-limit-1][o][1]) % MOD

                dp[z][o][1] = (dp[z][o-1][0] + dp[z][o-1][1]) % MOD
                if o > limit: dp[z][o][1] = (dp[z][o][1] - dp[z][o-limit-1][0]) % MOD

        return (dp[zero][one][0] + dp[zero][one][1]) % MOD