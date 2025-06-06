class Solution:
    def climbStairs(self, n: int) -> int:
        return self.helper(n, {})
    
    def helper(self, n, memo):
        if n == 0 or n == 1: return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]
            