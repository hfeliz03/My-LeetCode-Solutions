class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        if all(num <= 0 for num in nums) : return max(nums)
        curMax = nums[0]
        curSum = 0
        for num in nums:
            if curSum + num <= 0: 
                curSum = 0
                continue
            else: 
                curSum += num

            curMax = max(curMax, curSum)
        
        return curMax