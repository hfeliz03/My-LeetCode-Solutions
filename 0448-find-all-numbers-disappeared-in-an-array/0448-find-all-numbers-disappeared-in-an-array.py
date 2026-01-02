class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        disappeared = set(range(1,len(nums)+1)) - set(nums)
        return list(disappeared)