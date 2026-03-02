class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # dp[i+1] and dp[i+2] rolling
        dp1 = 1 if s[-1] != '0' else 0  # dp[n-1]
        dp2 = 1                         # dp[n] (empty string)

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                cur = 0
            else:
                cur = dp1  # take one digit
                two = int(s[i:i+2])
                if 10 <= two <= 26:
                    cur += dp2  # take two digits
            dp2, dp1 = dp1, cur

        return dp1
