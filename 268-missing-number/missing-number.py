class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        setNums = set(range(n+1))
        print(setNums)
        for i in nums:
            setNums.discard(i)

        return setNums.pop()