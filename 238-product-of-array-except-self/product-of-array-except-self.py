class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = []
        postfix = [1]*n

        curProduct = 1
        for i in nums:
            curProduct *= i
            prefix.append(curProduct)

        curProduct = 1
        for i in range(n)[::-1]:
            curProduct *= nums[i]
            postfix[i] = curProduct

        res = []
        for i in range(n):
            if i-1 < 0:
                res.append(postfix[i+1])
            elif i+1 >= n: 
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1] * postfix[i+1])
        
        return res