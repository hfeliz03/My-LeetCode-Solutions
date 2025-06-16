class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1 : return nums[0]
        if len(nums) == 2 : return max(nums[1], nums[0])
        rob1, rob2 = 0, 0
        
        for num in nums:
            currMax = max(rob2, rob1 + num)
            rob1 = rob2 
            rob2 = currMax
        return rob2