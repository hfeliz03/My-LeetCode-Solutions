class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        @cache
        def dp(i, gcd1, gcd2):
            if i == len(nums):
                if gcd1 == gcd2: return 1
                else: return 0

            total = 0
            total = (total + dp(i+1, gcd1, gcd2)) % MOD
            total = (total + dp(i+1, gcd(gcd1, nums[i]), gcd2)) % MOD       
            total = (total + dp(i+1, gcd1, gcd(gcd2, nums[i]))) % MOD

            return total 
        
        return (dp(0,0,0) - 1) % MOD