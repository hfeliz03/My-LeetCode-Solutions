class Solution:
    def reverseBits(self, n: int) -> int:
        binaryString = bin(n)[2:].zfill(32)
        reversedBinaryString = binaryString[::-1] 
        return int(reversedBinaryString, 2)