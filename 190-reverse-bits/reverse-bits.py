class Solution:
    def reverseBits(self, n: int) -> int:
        nbin = bin(n)[2:].zfill(32)    
        nbinrev = nbin[::-1]
        return int(nbinrev,2)