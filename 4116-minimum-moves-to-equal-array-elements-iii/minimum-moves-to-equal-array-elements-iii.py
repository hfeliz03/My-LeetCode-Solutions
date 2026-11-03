class Solution:
    def minMoves(self, nums: List[int]) -> int:
        maxNum = max(nums)
        res = 0
        for num in nums: 
            res += maxNum - num if maxNum - num > 0 else 0
        return res