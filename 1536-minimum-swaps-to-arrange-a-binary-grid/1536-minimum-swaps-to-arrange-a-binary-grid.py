class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        #This one was very hard for me
        n = len(grid)

        # trailing zeros per row
        tz = []
        for r in range(n):
            cnt = 0
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 0:
                    cnt += 1
                else:
                    break
            tz.append(cnt)

        swaps = 0
        for i in range(n):
            need = n - 1 - i

            # find first row j >= i with enough trailing zeros
            j = i
            while j < n and tz[j] < need:
                j += 1
            if j == n:
                return -1

            # bubble row j up to i
            while j > i:
                tz[j], tz[j - 1] = tz[j - 1], tz[j]
                swaps += 1
                j -= 1

        return swaps