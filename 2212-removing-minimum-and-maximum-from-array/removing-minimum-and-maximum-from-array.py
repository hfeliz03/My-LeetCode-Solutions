class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minNum, maxNum = 10**10, -10**10
        minNumIndex, maxNumIndex = -1, -1
        n = len(nums)

        for i, num in enumerate(nums):
            if num < minNum:
                minNum = num
                minNumIndex = i
            if num > maxNum:
                maxNum = num
                maxNumIndex = i

        return min( (n - minNumIndex) + (maxNumIndex + 1), (n - maxNumIndex) + (minNumIndex + 1), max(minNumIndex, maxNumIndex) + 1,  n - min(minNumIndex, maxNumIndex) )
