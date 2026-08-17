# The O(n^3) solution was doable, the optimal is some bs fr
class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        ps = [stoneValue[0]] * n
        for i in range(1, n): 
            ps[i] = ps[i - 1] + stoneValue[i]
        
        dp = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]

        for i in range(n):
            left[i][i] = stoneValue[i]
            right[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                total = ps[r] - (ps[l - 1] if l - 1 >= 0 else 0)
                target = (ps[l - 1] if l - 1 >= 0 else 0) + (total + 1) // 2
                mid = bisect_left(ps, target, l, r + 1)

                dp[l][r] = 0 if mid == l else left[l][mid - 1]
                ls = ps[mid] - (ps[l - 1] if l - 1 >= 0 else 0)
                if ls * 2 == total : dp[l][r] = max(left[l][mid], right[mid + 1][r])
                if ls * 2 == total:
                    dp[l][r] = max(
                        left[l][mid],
                        0 if mid == r else right[mid + 1][r]
                    )
                else: dp[l][r] = max(dp[l][r], 0 if mid == r else right[mid+1][r])
                
                value = total + dp[l][r]
                left[l][r] = max(left[l][r - 1], value)
                right[l][r] = max(right[l + 1][r], value)

        return dp[0][n-1]

        