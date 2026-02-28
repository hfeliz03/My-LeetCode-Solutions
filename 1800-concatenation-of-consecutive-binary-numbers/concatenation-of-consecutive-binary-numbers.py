class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = 0
        for i in range(1,n+1):
            res = ((res << (i).bit_length()) + i) % (10**9 + 7)
        return res  