#This is crazy, how am i supposed to get to this conclusion
class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        c0, c1, c2 = count

        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0

        return abs(c1 - c2) > 2