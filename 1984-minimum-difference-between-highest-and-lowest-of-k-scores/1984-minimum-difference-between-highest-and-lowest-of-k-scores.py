class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k <= 1: return 0

        n = len(nums)
        nums = sorted(nums)
        minDiff = 10**5

        for i in range(n - k + 1):
            minDiff = min(minDiff, nums[i+k-1] - nums[i])

        return minDiff