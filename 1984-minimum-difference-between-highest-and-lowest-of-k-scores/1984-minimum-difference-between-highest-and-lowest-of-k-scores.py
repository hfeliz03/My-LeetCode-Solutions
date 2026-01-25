class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums = sorted(nums)
        minDiff = 10**5
        for i in range(n - k + 1):
            window = nums[i:i+k]
            minWindow, maxWindow = window[0], window[-1]
            minDiff = min(minDiff, maxWindow - minWindow)

        return minDiff