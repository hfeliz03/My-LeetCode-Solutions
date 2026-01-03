class Solution:
    def numOfWays(self, n: int) -> int:
        # This was so cool to see, i didnt code this alone myself
        MOD = 10**9 + 7
        
        aba = 6  # patterns like R Y R. a can be 3 colors, thus b can be only the two other colors. 3*2 = 6
        abc = 6  # patterns like R Y G. a can be 3, b can be 2, c can be 1. 3*2*1=6
        
        for x in range(2, n + 1):
            aba, abc = (aba * 3 + abc * 2) % MOD, (aba * 2 + abc * 2) % MOD

        return (aba + abc) % MOD