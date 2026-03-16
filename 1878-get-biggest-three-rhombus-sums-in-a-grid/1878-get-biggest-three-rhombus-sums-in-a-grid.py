class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        # I didnt write all this code, the checking inside the rhombus was complicated
        n = len(grid)
        m = len(grid[0])
        res = set()

        for i in range(n): 
            for j in range(m):
                res.add(grid[i][j])

                s = 1
                while i - s * 2 >= 0 and j - s >= 0 and j + s < m:
                    acc = (
                        grid[i][j] #bot
                        + grid[i - s * 2][j] #top 
                        + grid[i - s][j - s] #left
                        + grid[i - s][j + s] #right
                    )

                    for step in range(1, s):
                        acc += (
                            grid[i - step][j - step] #bl
                            + grid[i - step][j + step] #br
                            + grid[i - s * 2 + step][j - step] #tl
                            + grid[i - s * 2 + step][j + step] #tr
                        )
                    
                    res.add(acc)
                    s += 1
        res = list(res)
        res.sort(reverse = True)
        return res[:3]