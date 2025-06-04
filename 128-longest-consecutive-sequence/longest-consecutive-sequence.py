class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0
        numSet = set(nums)
        if len(nums) == 1: return 1
        i =0

        totalCount, count = 1 , 1 
        for num in numSet:
            if num - 1 not in numSet:
                j = 1
                while num+j in numSet:
                    count+=1
                    j+=1
            totalCount = max(totalCount, count)
            count = 1

        return totalCount