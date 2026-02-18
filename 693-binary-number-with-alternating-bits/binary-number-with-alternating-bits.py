class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n = bin(n)[2:]
        for i in range(1,len(n)):
            if n[i-1] == n[i]: return False
        return True