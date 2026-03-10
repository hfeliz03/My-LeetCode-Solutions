class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums: 
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globalMax = max(globalMax, curMax)
            globalMin = min(globalMin, curMin)
        
        return max(globalMax, total - globalMin) if globalMax > 0 else max(nums)