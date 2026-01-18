class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        if not grid: 
            return 0

        m, n = len(grid), len(grid[0])
        largest = 1

        def checkMagicSquare(subGrid: List[List[int]]) -> bool:
            k = len(subGrid)
            target = sum(subGrid[0])

            cols = [0] * k
            d1 = 0
            d2 = 0

            for i in range(k):
                if sum(subGrid[i]) != target:
                    return False
                for j in range(k):
                    cols[j] += subGrid[i][j]
                    if i == j:
                        d1 += subGrid[i][j]
                d2 += subGrid[i][k - 1 - i]

            if d1 != target or d2 != target:
                return False

            for c in cols:
                if c != target:
                    return False

            return True

        # try bigger squares first so we can skip a lot
        for k in range(min(m, n), 1, -1):
            # if we already found >= k, no point checking smaller? (we're going downward anyway)
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    # build the kxk subgrid the right way
                    sub = [row[j:j+k] for row in grid[i:i+k]]
                    if checkMagicSquare(sub):
                        return k  # first found is max because we go k from big->small

        return largest