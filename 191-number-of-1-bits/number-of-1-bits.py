class Solution:
    def hammingWeight(self, n: int) -> int:
        binaryString, setBits = bin(n)[2:], 0
        for i in binaryString: 
            if i == "1": 
                setBits +=1
        return setBits