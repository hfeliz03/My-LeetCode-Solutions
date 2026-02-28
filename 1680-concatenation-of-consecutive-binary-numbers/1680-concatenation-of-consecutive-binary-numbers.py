class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ""
        for i in range(n):
            s += bin(i+1)[2:]
        return int(s,2) % (10**9 + 7)