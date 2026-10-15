class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                print(sum([num**2 for num in nums[i:j+1]]))
                res += len(set(nums[i:j+1]))** 2
        return res