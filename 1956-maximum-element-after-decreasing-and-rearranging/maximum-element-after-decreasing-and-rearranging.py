class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        if arr[0] != 1: arr[0] = 1
        n = len(arr)
        for i in range(1,n):
            if arr[i] > arr[i - 1] + 1: arr[i] = arr[i-1] + 1
        return arr[-1]