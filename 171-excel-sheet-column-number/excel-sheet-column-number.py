class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = len(columnTitle)
        res = 0
        for i, character in enumerate(columnTitle):
            res += (26**(n - i - 1)) * (ord(character) - 65 + 1)
        return res
