class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        if not grid: return False
        visitedCells = set()
        m, n = len(grid), len(grid[0])

        for row in range(m):
            for col in range(n):
                cell = (row, col)
                if cell in visitedCells: continue
                def dfs(cell, prevDir):
                    if cell in visitedCells:
                        return True
                    visitedCells.add(cell)
                    x, y = cell
                    if x + 1 < m and grid[x+1][y] == grid[x][y] and (x+1, y) != prevDir:
                        if dfs((x+1, y), (x, y)):
                            return True
                    if y + 1 < n and grid[x][y+1] == grid[x][y] and (x, y+1) != prevDir:
                        if dfs((x, y+1), (x, y)):
                            return True
                    if x - 1 >= 0 and grid[x-1][y] == grid[x][y] and (x-1, y) != prevDir:
                        if dfs((x-1, y), (x, y)):
                            return True
                    if y - 1 >= 0 and grid[x][y-1] == grid[x][y] and (x, y-1) != prevDir:
                        if dfs((x, y-1), (x, y)):
                            return True
                    return False
                if dfs(cell, (-1, -1)): 
                    return True
        return False
        