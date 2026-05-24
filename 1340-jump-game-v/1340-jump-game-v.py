class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        memo = {}

        def dfs(i):
            if i in memo: return memo[i]
            best = 1

            # left
            for j in range(i - 1, max(-1, i - d - 1), -1):
                if arr[j] >= arr[i]: break
                best = max(best, 1 + dfs(j))

            # right
            for j in range(i + 1, min(n, i + d + 1)):
                if arr[j] >= arr[i]: break
                best = max(best, 1 + dfs(j))

            memo[i] = best
            return best

        return max(dfs(i) for i in range(n))