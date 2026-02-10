class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            setEvens = {}
            setOdds = {}
            for j in range(i,n):
                if nums[j] % 2 == 1:
                    setOdds[nums[j]] = setOdds.get(nums[j], 0) + 1
                else:
                    setEvens[nums[j]] = setEvens.get(nums[j], 0) + 1
                if len(setEvens.keys()) == len(setOdds.keys()):
                    res = max(res, j-i+1)
        
        return res
            