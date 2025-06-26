class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32 bits all 1s
        MAX_INT = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (carry << 1) & MASK

        # If a is greater than MAX_INT, it's negative in two's complement
        return a if a <= MAX_INT else ~(a ^ MASK)
