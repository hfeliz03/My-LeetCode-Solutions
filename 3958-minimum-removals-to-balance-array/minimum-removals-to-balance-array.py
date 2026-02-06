class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1: return 0

        nums = sorted(nums)
        mx = 0

        l = 0
        for r in range(n):
            while l<r and nums[l] * k < nums[r]:
                l+=1
            mx = max(mx, r-l+1)

        return n - mx