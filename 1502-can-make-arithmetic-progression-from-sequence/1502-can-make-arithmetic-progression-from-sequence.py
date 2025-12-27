class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        currDiff, pastDiff = 0, 0
        for i, num in enumerate(arr):
            if i == 0:
                continue
            if i == 1:
                pastDiff = num - arr[i-1]
            currDiff = num - arr[i-1]
            if currDiff != pastDiff: return False
            pastDiff = currDiff
        return True
            

