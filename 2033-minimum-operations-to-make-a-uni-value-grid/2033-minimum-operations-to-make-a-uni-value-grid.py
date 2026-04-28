class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        if not grid: return 0
        flatSorted = sorted([element for row in grid for element in row])
        if len(flatSorted) <= 1: return 0

        for el in flatSorted:
           if el % x != flatSorted[0] % x: return -1

        mid = flatSorted[len(flatSorted) // 2]
        
        res = 0
        for el in flatSorted:
            res += abs(el - mid) // x

        return res
        