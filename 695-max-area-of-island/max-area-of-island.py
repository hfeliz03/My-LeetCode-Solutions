class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set() #(x,y)
        m, n = len(grid), len(grid[0])
        maxLen = 0


        curLen = 0
        def dfs(x, y):
            nonlocal curLen
            visited.add((x,y))
            curLen += 1
            if x + 1 < m and grid[x+1][y] == 1 and (x+1,y) not in visited:
                dfs(x+1, y)
            if y + 1 < n and grid[x][y+1] == 1 and (x,y+1) not in visited:
                dfs(x, y+1)
            if x - 1 >= 0 and grid[x-1][y] == 1 and (x-1,y) not in visited:
                dfs(x-1, y)
            if y - 1 >= 0 and grid[x][y-1] == 1 and (x,y-1) not in visited:
                dfs(x, y-1)

        for x in range(m):
            for y in range(n):
                if (x,y) not in visited and grid[x][y] == 1:
                    #bfs/dfs
                    curLen = 0
                    dfs(x, y)
                    maxLen = max(maxLen, curLen)
        
        return maxLen 