class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        res = -1
        curMin = 10**10
        n = len(nums)
        for i in range(n):
            instability = max(nums[:i+1]) - min(nums[i:n]) 
            if instability <= k: 
                res = i
                break
        return res