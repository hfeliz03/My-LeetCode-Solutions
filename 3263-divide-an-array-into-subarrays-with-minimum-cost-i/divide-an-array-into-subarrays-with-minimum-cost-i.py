class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        n = len(nums)
        suffixMin = [0] * n
        suffixMin[-1] = nums[-1]
        for k in range(n - 2, -1, -1):
            suffixMin[k] = min(nums[k], suffixMin[k + 1])

        best = float("inf")
        for i in range(1, n - 1):          # i can go up to n-2, but i=n-1 invalid anyway
            if i <= n - 2:
                best = min(best, nums[i] + suffixMin[i + 1])

        return nums[0] + best