class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        cur = 0

        for i, num in enumerate(nums):
            cur += i * num

        res = cur

        for k in range(1, n):
            cur = cur + total - n * nums[n - k]
            res = max(res, cur)
        return res