#Absolute pain to write ts
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        if not grid: return False
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(x, y, xprev, yprev):
            if (x, y) in visited:
                return False
            visited.add((x, y))
            if x == m - 1 and y == n - 1:
                return True
            if grid[x][y] == 1: # left/right
                if yprev == y - 1: # from left, go right
                    if y + 1 < n and grid[x][y+1] in {1, 3, 5}:
                        return dfs(x, y+1, x, y)
                else: # from right, go left
                    if y - 1 >= 0 and grid[x][y-1] in {1, 4, 6}:
                        return dfs(x, y-1, x, y)
            if grid[x][y] == 2: # up/down
                if xprev == x - 1: # from up, go down
                    if x + 1 < m and grid[x+1][y] in {2, 5, 6}:
                        return dfs(x+1, y, x, y)
                else: # from down, go up
                    if x - 1 >= 0 and grid[x-1][y] in {2, 3, 4}:
                        return dfs(x-1, y, x, y)
            if grid[x][y] == 3: # left/down
                if yprev == y - 1: # from left, go down
                    if x + 1 < m and grid[x+1][y] in {2, 5, 6}:
                        return dfs(x+1, y, x, y)
                else: # from down, go left
                    if y - 1 >= 0 and grid[x][y-1] in {1, 4, 6}:
                        return dfs(x, y-1, x, y)
            if grid[x][y] == 4: # right/down
                if yprev == y + 1: # from right, go down
                    if x + 1 < m and grid[x+1][y] in {2, 5, 6}:
                        return dfs(x+1, y, x, y)
                else: # from down, go right
                    if y + 1 < n and grid[x][y+1] in {1, 3, 5}:
                        return dfs(x, y+1, x, y)
            if grid[x][y] == 5: # left/up
                if yprev == y - 1: # from left, go up
                    if x - 1 >= 0 and grid[x-1][y] in {2, 3, 4}:
                        return dfs(x-1, y, x, y)
                else: # from up, go left
                    if y - 1 >= 0 and grid[x][y-1] in {1, 4, 6}:
                        return dfs(x, y-1, x, y)
            if grid[x][y] == 6: # right/up
                if yprev == y + 1: # from right, go up
                    if x - 1 >= 0 and grid[x-1][y] in {2, 3, 4}:
                        return dfs(x-1, y, x, y)
                else: # from up, go right
                    if y + 1 < n and grid[x][y+1] in {1, 3, 5}:
                        return dfs(x, y+1, x, y)
            return False
        # start case: try possible first moves from (0,0)
        if m == 1 and n == 1:
            return True
        if grid[0][0] in {1, 4, 6}: # can go right
            if n > 1 and grid[0][1] in {1, 3, 5}:
                if dfs(0, 1, 0, 0):
                    return True
        if grid[0][0] in {2, 3, 4}: # can go down
            if m > 1 and grid[1][0] in {2, 5, 6}:
                if dfs(1, 0, 0, 0):
                    return True
        return False