class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count1s(n):
            return Counter(bin(n)[2:])["1"]

        return [count1s(bits) for bits in range(n+1)]