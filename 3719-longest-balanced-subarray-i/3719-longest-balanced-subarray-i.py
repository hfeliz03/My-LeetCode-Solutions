class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            setEvens = set()
            setOdds = set()
            for j in range(i,n):
                if nums[j] % 2 == 1:
                    setOdds.add(nums[j])
                else:
                    setEvens.add(nums[j])
                if len(setEvens) == len(setOdds):
                    res = max(res, j-i+1)
        
        return res
            