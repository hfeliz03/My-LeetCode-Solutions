class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        ans = 0

        def is_magic(r: int, c: int) -> bool:
            # collect 3x3
            vals = [grid[r+i][c+j] for i in range(3) for j in range(3)]

            # must be digits 1..9 exactly once
            if set(vals) != set(range(1, 10)):
                return False

            # (optional fast prune) center must be 5 in any 1..9 magic square
            if grid[r+1][c+1] != 5:
                return False

            s = 15
            # rows
            if grid[r][c] + grid[r][c+1] + grid[r][c+2] != s: return False
            if grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] != s: return False
            if grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] != s: return False
            # cols
            if grid[r][c] + grid[r+1][c] + grid[r+2][c] != s: return False
            if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != s: return False
            if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != s: return False
            # diags
            if grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] != s: return False
            if grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c] != s: return False

            return True

        for r in range(R - 2):
            for c in range(C - 2):
                if is_magic(r, c):
                    ans += 1

        return ans
                