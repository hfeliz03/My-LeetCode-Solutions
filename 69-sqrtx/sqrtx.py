class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        for i in range((x//2)+2):
            if i*i == x : return i
            if i*i>x: return i-1