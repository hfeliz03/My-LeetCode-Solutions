class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= m or y >= n:
                return False

            if grid[x][y] == 1 or (x, y) in visited:
                return True

            visited.add((x, y))

            down = dfs(x + 1, y)
            up = dfs(x - 1, y)
            right = dfs(x, y + 1)
            left = dfs(x, y - 1)

            return down and up and right and left

        res = 0

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0 and (x, y) not in visited:
                    if dfs(x, y):
                        res += 1

        return res