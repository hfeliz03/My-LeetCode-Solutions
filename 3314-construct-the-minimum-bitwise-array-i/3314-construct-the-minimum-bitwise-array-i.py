class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n    
        for i in range(n):
            curNum = nums[i]
            if curNum % 2 == 0: continue
            j = 0
            while j < curNum:
                if (j | (j+1)) == curNum:
                    ans[i] = j
                    break
                j+=1
            
        return ans