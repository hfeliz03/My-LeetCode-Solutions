class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefixSum = []
        for i, stone in enumerate(stones):
            if i == 0: prefixSum.append(stone)
            else: prefixSum.append(stone + prefixSum[-1])

        n = len(stones)
        dp = [0] * n
        dp[-1] = prefixSum[-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], prefixSum[i] - dp[i+1])
        return dp[1]