class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        flat = [element for row in grid for element in row]
        print(flat)
        nm = len(flat)
        k %= nm
        shifted = flat[nm - k:] + flat[:nm-k]
        print(shifted)
        m, n = len(grid), len(grid[0])
        res = []
        while len(res) < m:
            res.append(shifted[(len(res))*n :(1+len(res))*n])
        return res