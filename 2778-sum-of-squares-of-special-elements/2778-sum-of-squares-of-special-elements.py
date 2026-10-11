class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        for i, num in enumerate(nums): 
            if len(nums) % (i+1)== 0: 
                res += num**2
        return res