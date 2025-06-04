class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        if not nums: return 0
        if len(nums) == 1: return 1
    

        i, totalCount, count = 0, 1 , 1 
        for num in numSet:
            if num - 1 not in numSet:
                j = 1
                while num+j in numSet:
                    count+=1
                    j+=1
            totalCount = max(totalCount, count)
            count = 1

        return totalCount