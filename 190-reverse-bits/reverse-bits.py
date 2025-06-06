class Solution:
    def reverseBits(self, n: int) -> int:
        binaryString = bin(n)[2:].zfill(32)
        reversedBinaryString =""
        i = -1
        while -i <= len(binaryString):
            reversedBinaryString += binaryString[i]
            i -=1
        return int(reversedBinaryString, 2)