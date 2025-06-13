class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1: return 1
        for i in range(x//2+2): 
            if i*i <= x and (i+1)*(i+1)>x: return i