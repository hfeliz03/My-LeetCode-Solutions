class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for i in range(2**31 - 1):
            if 4**i == n: return True
            if 4**i > n : return False