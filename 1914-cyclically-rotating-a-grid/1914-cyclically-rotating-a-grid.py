class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        #These indices where so hard
        n, m = len(grid), len(grid[0])

        for layer in range(min(n // 2, m // 2)):
            items = []

            for j in range(layer, m - layer):
                items.append(grid[layer][j])

            for i in range(layer + 1, n - layer):
                items.append(grid[i][m-layer-1])
            
            for j in range(m - layer - 2, layer - 1, -1):
                items.append(grid[n - layer - 1][j])
            
            for i in range(n - layer - 2, layer, -1):
                items.append(grid[i][layer])
            
            nk = k % len(items)
            items = items[nk:] + items[:nk]

            idx = 0
            for j in range(layer, m - layer):
                grid[layer][j] = items[idx]
                idx += 1

            for i in range(layer + 1, n - layer):
                grid[i][m-layer-1] = items[idx]
                idx += 1
            
            for j in range(m - layer - 2, layer - 1, -1):
                grid[n - layer - 1][j] = items[idx]
                idx += 1
            
            for i in range(n - layer - 2, layer, -1):
                grid[i][layer] = items[idx]
                idx += 1

        return grid