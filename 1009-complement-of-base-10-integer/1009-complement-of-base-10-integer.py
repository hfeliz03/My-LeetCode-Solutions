class Solution:
    def bitwiseComplement(self, n: int) -> int:
        inBin = bin(n)[2:]
        comp = ""
        for c in inBin:
            if c == "1": 
                comp += "0"
            else: 
                comp += "1"
        return int(comp,2)