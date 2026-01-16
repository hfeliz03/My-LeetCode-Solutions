class Solution:
    def maximizeSquareArea(self, m: int, n: int, hFences: List[int], vFences: List[int]) -> int:
        hFences += [1, m] 
        vFences += [1, n]

        hFencesDiff = set()
        for indexI, i in enumerate(hFences):
            for j in hFences[indexI+1:]:
                hFencesDiff.add(abs(j - i))
        
        curMaxSquare = -1
        for indexI, i in enumerate(vFences):
            for j in vFences[indexI+1:]:
                if (abs(j-i) in hFencesDiff):
                    curMaxSquare = max(curMaxSquare, abs(j-i))
        
        return (curMaxSquare ** 2) % (10**9 + 7) if curMaxSquare > 0 else -1
