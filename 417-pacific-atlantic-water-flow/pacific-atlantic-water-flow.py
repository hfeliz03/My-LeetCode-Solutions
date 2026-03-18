class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac = set()
        atl = set()

        def bfs(r, c, ocean, prevHeight):
            if r < 0 or c < 0 or r >= rows or c >= cols:
                return
            if (r, c) in ocean:
                return
            if heights[r][c] < prevHeight:
                return

            ocean.add((r, c))
            bfs(r + 1, c, ocean, heights[r][c])
            bfs(r - 1, c, ocean, heights[r][c])
            bfs(r, c + 1, ocean, heights[r][c])
            bfs(r, c - 1, ocean, heights[r][c])

        for c in range(cols):
            bfs(0, c, pac, heights[0][c])
            bfs(rows - 1, c, atl, heights[rows - 1][c])

        for r in range(rows):
            bfs(r, 0, pac, heights[r][0])
            bfs(r, cols - 1, atl, heights[r][cols - 1])

        return [list(cell) for cell in pac & atl]