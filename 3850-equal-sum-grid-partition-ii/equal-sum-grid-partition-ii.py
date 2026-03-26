class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        # def check(g):
        #     nn = len(g)
        #     mm = len(g[0])

        #     curr = 0
        #     seen = {} #seen[v] = {firstseen, lastseen}
        #     for i in range(nn-1):
        #         for j in range(mm):
        #             v = g[i][j]
        #             curr += v
        #             if v in seen: seen[v][1] = (i,j)
        #             else: seen[v] = [(i,j), (i,j)]
        #         diff = total - curr - curr
        #         if diff == 0: return True
        #         if -diff in seen:
        #             fr, fc = seen[-diff][0]
        #             lr, lc = seen[-diff][1]
        #             if mm > 1 and i + 1 > 1: return True # big grid, always connected
        #             if mm > 1 and i + 1 == 1 and (fc == 0 or lc == mm -1): return True
        #             if mm == 1 and (fr == 0 or lr == i): return True # one col
        def check(grid):
            topSum = 0
            seen = set()
            for i in range(len(grid)-1):
                for j in range(len(grid[0])): seen.add(grid[i][j])
                topSum+=sum(grid[i])
                diff = 2*topSum - total
                if diff == 0: return True
                if grid[0][0] == diff or grid[0][-1] == diff or grid[i][0] == diff: return True
                if diff in seen and i>0 and len(grid[0])>1: return True
            return False

        n = len(grid)
        m = len(grid[0])

        total = sum(grid[i][j] for j in range(m) for i in range(n))
        if check(grid) or check(grid[::-1]): return True

        grid = list(zip(*grid)) #Beautiful way to transpose the matrix

        if check(grid) or check(grid[::-1]): return True
        return False
