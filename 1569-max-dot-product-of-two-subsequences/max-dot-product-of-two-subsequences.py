class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [float("-inf")] * (n+1)

        for i in range(m - 1, -1, -1):
            new = [float("-inf")] * (n + 1)
            for j in range(n-1, -1, -1):
                prod = nums1[i]*nums2[j]

                take = prod
                if dp[j+1] > 0:
                    take += dp[j+1]
                
                new[j] = max(
                    take, 
                    dp[j],
                    new[j+1]
                )
            dp = new
        

        return dp[0]