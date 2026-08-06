class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            prod = 1
            for char in str(n):
                prod *= int(char)
            if prod % t == 0: return n
            n += 1
        return