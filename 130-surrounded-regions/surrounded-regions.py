class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        surrounded = set()
        safe = False
        m, n = len(board), len(board[0])


        def surround():
            nonlocal surrounded
            while surrounded:
                x, y = surrounded.pop()
                board[x][y] = "X"

        def dfs(x,y):
            nonlocal surrounded
            nonlocal visited
            visited.add((x,y))
            surrounded.add((x,y))
            if x == 0 or x == m-1 or y == 0 or y == n-1: #then its in the border, i.e. not surrounded
                nonlocal safe
                safe = True
            if x + 1 < m and board[x+1][y] == "O" and (x + 1,y) not in visited:
                dfs(x+1, y)
            if x - 1 >= 0  and board[x-1][y] == "O" and (x - 1,y) not in visited:
                dfs(x-1, y)
            if y + 1 < n and board[x][y+1] == "O" and (x,y + 1) not in visited:
                dfs(x, y+1)
            if y - 1 >= 0 and board[x][y-1] == "O" and (x,y - 1) not in visited:
                dfs(x, y-1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O" and (i,j) not in visited:
                    surrounded = set()
                    dfs(i, j)
                    if not safe: surround()
                    safe = False

        return