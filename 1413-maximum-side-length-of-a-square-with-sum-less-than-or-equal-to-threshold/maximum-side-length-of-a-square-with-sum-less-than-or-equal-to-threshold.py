class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # 2D prefix sum: ps[i+1][j+1] = sum of rectangle (0,0) .. (i,j)
        ps = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            row_acc = 0
            for j in range(n):
                row_acc += mat[i][j]
                ps[i + 1][j + 1] = ps[i][j + 1] + row_acc

        def square_sum(r: int, c: int, k: int) -> int:
            # sum of kxk square with top-left (r,c)
            r2, c2 = r + k, c + k
            return ps[r2][c2] - ps[r][c2] - ps[r2][c] + ps[r][c]

        def exists(k: int) -> bool:
            # any kxk square with sum <= threshold?
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if square_sum(i, j, k) <= threshold:
                        return True
            return False

        lo, hi = 0, min(m, n)
        while lo < hi:
            mid = (lo + hi + 1) // 2  # try bigger
            if exists(mid):
                lo = mid
            else:
                hi = mid - 1

        return lo