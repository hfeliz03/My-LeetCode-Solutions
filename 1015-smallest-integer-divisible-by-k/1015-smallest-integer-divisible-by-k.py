class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # n can only contain 1. 1, 11, 111, 1111
        # Return length of smallest possible int s.t. n%k==0
        # Impossible cases
        if k % 2 == 0 or k % 5 == 0:
            return -1

        remainder = 0
        for length in range(1, k + 1):
            remainder = (remainder * 10 + 1) % k
            if remainder == 0:
                return length

        return -1