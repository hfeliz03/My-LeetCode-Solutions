class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences += [1, m] 
        vFences += [1, n]

        hFencesDiff = set()
        for indexI, i in enumerate(hFences):
            for j in hFences[indexI+1:]:
                hFencesDiff.add(abs(j - i))
        
        vFencesDiff = set()
        for indexI, i in enumerate(vFences):
            for j in vFences[indexI+1:]:
                vFencesDiff.add(abs(j - i))
        
        possibleSquares = hFencesDiff & vFencesDiff
        return (max(possibleSquares) ** 2) % (10**9 + 7) if len(possibleSquares) > 0 else -1
