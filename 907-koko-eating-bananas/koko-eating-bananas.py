import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        upperBoundSpeed = r
        

        while l <= r:
            midSpeed = l + (r-l)//2
            hCount = 0

            for pile in piles:
                hCount += math.ceil(pile / (midSpeed))
                if hCount > h: break

            if hCount <= h:
                upperBoundSpeed = midSpeed
                r = midSpeed - 1
            else:
                l = midSpeed + 1

        return upperBoundSpeed
