class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def can_cross(day: int) -> bool:
            # 0 = land, 1 = water
            grid = [[0 for _ in range(col)] for _ in range(row)]
            for k in range(day):  # first 'day' cells become water
                r, c = cells[k]
                grid[r - 1][c - 1] = 1

            q = deque()
            seen = [[False for _ in range(col)] for _ in range(row)]

            # start from any land cell in top row
            for j in range(col):
                if grid[0][j] == 0:
                    q.append((0, j))
                    seen[0][j] = True

            dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while q:
                r, c = q.popleft()
                if r == row - 1:
                    return True
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < row and 0 <= nc < col and not seen[nr][nc] and grid[nr][nc] == 0:
                        seen[nr][nc] = True
                        q.append((nr, nc))

            return False

        lo, hi = 0, len(cells)  # days in [0..n]
        while lo < hi:
            mid = (lo + hi + 1) // 2
            if can_cross(mid):
                lo = mid
            else:
                hi = mid - 1
        return lo