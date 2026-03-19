class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        #Check from 0,0 
        #keep track of the number of Xs and Ys at each i,j
        # 1,0  1,1  1,1 
        # 1,1. 1,2. 1,2
        m, n = len(grid), len(grid[0])
        tracker = [[0] * n for _ in range(m)]
        xTracker = [[0] * n for _ in range(m)]
        res = 0

        for i in range(m):
            for j in range(n):
                cur = 1 if grid[i][j] == "X" else -1 if grid[i][j] == "Y" else 0
                curX = 1 if grid[i][j] == "X" else 0

                if i == 0 and j == 0:
                    tracker[i][j] = cur
                    xTracker[i][j] = curX
                elif i == 0:
                    tracker[i][j] = tracker[i][j-1] + cur
                    xTracker[i][j] = xTracker[i][j-1] + curX
                elif j == 0:
                    tracker[i][j] = tracker[i-1][j] + cur
                    xTracker[i][j] = xTracker[i-1][j] + curX
                else:
                    tracker[i][j] = tracker[i-1][j] + tracker[i][j-1] - tracker[i-1][j-1] + cur
                    xTracker[i][j] = xTracker[i-1][j] + xTracker[i][j-1] - xTracker[i-1][j-1] + curX

                if tracker[i][j] == 0 and xTracker[i][j] > 0:
                    res += 1

        return res