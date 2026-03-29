from collections import Counter
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Build trie
        trie = {}
        for word in words:
            cur = trie
            for ch in word:
                cur = cur.setdefault(ch, {})
            cur["*"] = word   # store full word at end

        m, n = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            ch = board[i][j]

            if ch not in node:
                return

            nxt = node[ch]

            # Found a word
            if "*" in nxt:
                res.append(nxt["*"])
                del nxt["*"]   # avoid duplicates

            # Mark visited
            board[i][j] = "#"

            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != "#":
                    dfs(ni, nj, nxt)

            # Restore
            board[i][j] = ch

            # Optional pruning: remove empty branches from trie
            if not nxt:
                del node[ch]

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie)

        return res