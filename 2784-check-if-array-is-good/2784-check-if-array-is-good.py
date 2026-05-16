class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        seen = set()
        duplicate_max = False
        for x in nums:
            if x < 1 or x > n - 1: return False
            if x in seen:
                if x == n - 1: duplicate_max = True
                else: return False
            seen.add(x)
        return len(seen) == n - 1 and duplicate_max
            