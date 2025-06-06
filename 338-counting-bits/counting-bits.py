class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def count1s(n):
            count = 0
            for i in bin(n)[2:]:
                if i == "1": count +=1
            return count

        return [count1s(bits) for bits in range(n+1)]