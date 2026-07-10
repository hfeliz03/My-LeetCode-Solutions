class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        lastSeen = {}
        for i, num in enumerate(nums):
            if num in lastSeen and i - lastSeen[num] <= k: return True
            lastSeen[num] = i
        return False
        