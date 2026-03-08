class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        keep = arr[0]   # max sum ending here with no deletion
        drop = float('-inf')  # max sum ending here with one deletion used
        ans = arr[0]

        for i in range(1, len(arr)):
            drop = max(keep, drop + arr[i])
            keep = max(arr[i], keep + arr[i])
            ans = max(ans, keep, drop)

        return ans
        