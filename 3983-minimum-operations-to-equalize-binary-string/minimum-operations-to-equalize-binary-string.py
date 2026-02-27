class Solution:
    def minOperations(self, s: str, k: int) -> int:
        ### DID NOT SOLVE THIS
        n = len(s)
        z, o = 0 , 0 

        for c in s:
            if c == "0": z += 1
            else: o += 1
        if z == 0: return 0

        for op in range(1, n+1):
            flips = op * k
            if (flips - z) % 2 == 1: continue
        
            if op % 2 == 0 : 
                if z <= flips <= z * (op -1 ) + o * op : return op
            else: 
                if z <= flips <= z * op + o * (op - 1) : return op
        
        return -1