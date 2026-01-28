class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        #I DID NOT SOLVE THIS MYSELF
        if not grid: return 0
        n, m = len(grid), len(grid[0])
        cost = [[inf] * m for _ in range(n)] #cost[i][j] minimum cost to reach destination
        cost[-1][-1] = 0 #At the destination, the cost to reach itself is 0 ofc
        tcost = [inf] * (max(max(row) for row in grid) + 1)

        for t in range(k+1):
            for i in range(n-1, -1, -1):
                for j in range(m-1, -1, -1):
                    #Can move right, down or teleport
                    if i < n-1 : cost[i][j] = min(cost[i][j], cost[i+1][j] + grid[i+1][j])
                    if j < m-1 : cost[i][j] = min(cost[i][j], cost[i][j+1] + grid[i][j+1])
                    if t > 0: cost[i][j] = min(cost[i][j], tcost[grid[i][j]])

            # compute tcost for next t
            for i in range(n):
                for j in range(m):
                    tcost[grid[i][j]] = min(tcost[grid[i][j]], cost[i][j])

            for i in range(1, len(tcost)): 
                tcost[i] = min(tcost[i], tcost[i-1]) #Compute pref min
            
        return cost[0][0]

        


            




