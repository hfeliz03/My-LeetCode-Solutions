class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000: return 0
        else: return n - 1000 + 1