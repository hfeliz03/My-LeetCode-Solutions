class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if not nums: return None
        if len(nums) == 1: return nums[0]
        carry = 0
        for num in nums:
            carry = carry ^ num
        return carry