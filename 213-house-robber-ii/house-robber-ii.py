class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) ==1 : return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        
        def robHelper(nums):
            rob1, rob2 = 0, 0
            for i in range(0, len(nums)):
                temp = max(rob2, nums[i] + rob1)
                rob1 = rob2
                rob2 = temp
            return rob2  
        
        return max(robHelper(nums[0:len(nums)-1]), robHelper(nums[1:]))