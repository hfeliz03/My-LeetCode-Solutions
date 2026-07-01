from collections import deque
from math import inf
import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return 0

        n, m = len(grid), len(grid[0])

        # Step 1: Multi-source BFS from every thief
        # dist[i][j] = distance from cell (i, j) to nearest thief
        dist = [[inf] * m for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        while q:
            i, j = q.popleft()
            cd = dist[i][j]

            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue

                if cd + 1 < dist[ni][nj]:
                    dist[ni][nj] = cd + 1
                    q.append((ni, nj))

        # Step 2: Max-heap path search
        # We want to maximize the minimum dist along the path
        h = [(-dist[0][0], 0, 0)]
        seen = {(0, 0)}

        while h:
            w, i, j = heapq.heappop(h)
            w = -w

            if i == n - 1 and j == m - 1:
                return w

            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if ni < 0 or ni >= n or nj < 0 or nj >= m or (ni, nj) in seen:
                    continue

                seen.add((ni, nj))

                # Safeness of this path is the minimum value seen so far
                small = min(w, dist[ni][nj])

                heapq.heappush(h, (-small, ni, nj))