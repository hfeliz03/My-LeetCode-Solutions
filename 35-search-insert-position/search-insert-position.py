class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums: return 0
        l,r, m = 0, len(nums)-1, len(nums)//2
        while l <= r:
            if nums[m] == target: return m
            if nums[m] > target: r = m-1
            else: l = m+1
            m = (r+l)//2
        return m+1 #It's easy to see why we are returning m, the +1 is given to the fact that if not found it shall be placed one space after than m
        