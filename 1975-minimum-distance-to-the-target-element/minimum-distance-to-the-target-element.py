class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        minDis = 10**5
        for i, num in enumerate(nums):
            if num == target: minDis = min(minDis, abs(i - start))
        return minDis
