class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def dfs(row: int, col: int) -> int:
            if dp[row][col] != 0:
                return dp[row][col]

            # The cell itself forms a path of length 1.
            longest = 1

            for dr, dc in directions:
                new_row = row + dr
                new_col = col + dc

                if (
                    0 <= new_row < rows
                    and 0 <= new_col < cols
                    and matrix[new_row][new_col] > matrix[row][col]
                ):
                    longest = max(
                        longest,
                        1 + dfs(new_row, new_col)
                    )

            dp[row][col] = longest
            return longest

        return max(
            dfs(row, col)
            for row in range(rows)
            for col in range(cols)
        )