class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        left = 0
        for i in range(len(n)):
            if n[i] == "1":
                left = i
                break
        
        maxDistance = 0
        for right in range(left, len(n)):
            if n[right] == "1":
                maxDistance = max(maxDistance, right - left)
                left = right
        
        return maxDistance