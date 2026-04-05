from collections import Counter
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        m = Counter(moves)
        return m['U'] == m['D'] and m["L"] == m["R"]