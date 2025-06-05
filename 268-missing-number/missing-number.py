class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        setNums = set(range(n+1))
        print(setNums)
        for i in setNums:
            if i not in nums: return i

        return 