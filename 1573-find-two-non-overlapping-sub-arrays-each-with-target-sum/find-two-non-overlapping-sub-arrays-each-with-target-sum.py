class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        # best[i] = shortest target-sum subarray ending at or before i
        best = [float("inf")] * n

        left = 0
        curSum = 0
        shortest = float("inf")
        res = float("inf")

        for right in range(n):
            curSum += arr[right]

            while curSum > target:
                curSum -= arr[left]
                left += 1

            if curSum == target:
                length = right - left + 1

                # Find a previous non-overlapping subarray
                if left > 0 and best[left - 1] != float("inf"):
                    res = min(res, length + best[left - 1])

                # Update shortest subarray we've seen
                shortest = min(shortest, length)

            best[right] = shortest

        return res if res != float("inf") else -1