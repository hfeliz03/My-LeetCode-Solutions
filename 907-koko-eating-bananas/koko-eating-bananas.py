import math 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #From [1,max[piles]] Koko cannot eat 0 and we are trying to minimize r
        l,r = 1, max(piles)
        upperBoundSpeed = r
        

        while l <= r:
            #Binary search on Koko's possible speeds
            midSpeed = l + (r-l)//2
            hCount = 0

            #For each pile, we want to see how many hours it'll take to eat a given speed.
            for pile in piles:
                hCount += math.ceil(pile / (midSpeed))
                if hCount > h: break

            #If Koko was able to finish all the piles under the given time, we have a new best
            if hCount <= h:
                upperBoundSpeed = midSpeed
                #Check if there may be a slower speed that allows Koko to eat all the piles
                r = midSpeed - 1
            #Couldn't eat all the piles, increase speed
            else:
                l = midSpeed + 1

        return upperBoundSpeed
