class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        
        aba = 6  # patterns like R Y R
        abc = 6  # patterns like R Y G
        
        for _ in range(2, n + 1):
            new_aba = (aba * 3 + abc * 2) % MOD
            new_abc = (aba * 2 + abc * 2) % MOD
            aba, abc = new_aba, new_abc

        return (aba + abc) % MOD