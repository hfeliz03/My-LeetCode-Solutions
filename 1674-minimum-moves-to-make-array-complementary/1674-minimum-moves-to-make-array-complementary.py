class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        #Hard problem, didnt solve by myself
        n = len(nums)
        diff = [0] * (2 * limit + 2)
        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]
            low = 1 + min(a, b)
            high = limit + max(a, b)
            exact = a + b
            # Start assuming this pair needs 2 moves for every sum
            diff[2] += 2
            diff[2 * limit + 1] -= 2
            # For sums in [low, high], it needs only 1 move
            diff[low] -= 1
            diff[high + 1] += 1
            # For exact sum, it needs 0 moves
            diff[exact] -= 1
            diff[exact + 1] += 1
        ans = float("inf")
        cur = 0
        for s in range(2, 2 * limit + 1):
            cur += diff[s]
            ans = min(ans, cur)
        return ans