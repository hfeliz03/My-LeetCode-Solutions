class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        setNumsMiss = set(nums)
        fullSetNums = set(range(len(nums)+1))
        return (fullSetNums - setNumsMiss).pop()