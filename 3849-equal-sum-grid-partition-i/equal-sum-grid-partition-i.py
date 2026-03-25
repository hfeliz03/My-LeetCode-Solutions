class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        row_sums = [sum(row) for row in grid]
        col_sums = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        total = sum(row_sums)

        top = 0
        for i in range(m - 1):   # cut after row i
            top += row_sums[i]
            if top == total - top:
                return True

        left = 0
        for j in range(n - 1):   # cut after col j
            left += col_sums[j]
            if left == total - left:
                return True

        return False