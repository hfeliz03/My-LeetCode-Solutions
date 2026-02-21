class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0]*(n+1)
        if n == 1 : return 1
        def helper(n):
            if n == 2: return 2
            elif n <= 1: return 1
            if memo[n] == 0: 
                memo[n] = helper(n-1) + helper(n-2)
            return memo[n]

        return helper(n-1) + helper(n-2)