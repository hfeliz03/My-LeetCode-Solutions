from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        start = health - grid[0][0]
        if start <= 0:
            return False

        q = deque([(0, 0)])
        visited = {(0, 0): start}

        while q:
            x, y = q.popleft()

            if (x, y) == (m - 1, n - 1):
                return True

            for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx, ny = x + dx, y + dy

                if not (0 <= nx < m and 0 <= ny < n):
                    continue

                new_health = visited[(x, y)] - grid[nx][ny]

                if new_health <= 0:
                    continue

                # First visit or found a better path
                if (nx, ny) not in visited or new_health > visited[(nx, ny)]:
                    visited[(nx, ny)] = new_health
                    q.append((nx, ny))

        return False