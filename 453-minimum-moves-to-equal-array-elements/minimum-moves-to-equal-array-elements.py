#This soln is incredibly clean wow
class Solution:
    def minMoves(self, nums: list[int]) -> int:
        minimum = min(nums)
        return sum(x - minimum for x in nums)