class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n <= 1 or k <= 1: return 0
        nums = sorted(nums)
        minDiff = 10**5
        for i in range(n - k + 1):
            window = nums[i:i+k]
            minWindow, maxWindow = min(window), max(window)
            minDiff = min(minDiff, maxWindow - minWindow)

        return minDiff