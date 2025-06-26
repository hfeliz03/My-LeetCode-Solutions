class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        l,r = 0, len(nums)-1
        m = len(nums)//2
        while l <= r:
            if nums[m]==target: return m
            if nums[m] > target: r = m-1
            else: l = m+1
            m = (r+l)//2
        return m+1
        