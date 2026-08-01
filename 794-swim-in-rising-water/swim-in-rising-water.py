class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = {(0,0)}
        neighbors = {grid[0][0]: (0,0)} # elevation: (x,y)
        neighborsHeap = [grid[0][0]]
        heapq.heapify(neighborsHeap)
        t = grid[0][0]
        m, n = len(grid), len(grid[0])
        flag = False
        while t<m*n:
            x, y = neighbors[neighborsHeap[0]]
            if neighborsHeap[0] <= t:
                if (x, y) == (m - 1, n - 1): return t
                del neighbors[neighborsHeap[0]]
                heapq.heappop(neighborsHeap)
                if x+1 < m and (x+1, y) not in visited:
                    visited.add((x+1,y)) 
                    neighbors[grid[x+1][y]] = (x+1, y)
                    heapq.heappush(neighborsHeap,grid[x+1][y])
                if x-1 >= 0 and (x-1, y) not in visited: 
                    visited.add((x-1,y))
                    neighbors[grid[x-1][y]] = (x-1, y)
                    heapq.heappush(neighborsHeap,grid[x-1][y])
                if y+1 < n and (x, y+1) not in visited: 
                    visited.add((x,y+1))
                    neighbors[grid[x][y+1]] = (x, y+1)
                    heapq.heappush(neighborsHeap,grid[x][y+1])
                if y-1 >= 0 and (x, y-1) not in visited: 
                    visited.add((x,y-1))
                    neighbors[grid[x][y-1]] = (x, y-1)
                    heapq.heappush(neighborsHeap,grid[x][y-1])
                continue
            t += 1

        return t