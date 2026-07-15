class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return gcd(sum([x for x in range(n*2) if x % 2 == 0]), sum([x for x in range(n*2) if x % 2 == 1]))