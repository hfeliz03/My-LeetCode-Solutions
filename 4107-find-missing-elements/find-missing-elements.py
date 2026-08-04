class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        allNums = list(range(min(nums), max(nums)+1)) 
        nums = set(nums)
        res = [num for num in allNums if num not in nums]
        return res