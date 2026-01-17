class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        n = len(bottomLeft)
        maxIntersectionArea = 0
        for i in range(n): 
            xbl1, ybl1 = bottomLeft[i]
            xtr1, ytr1 = topRight[i]
            for j in range(i+1, n):
                xbl2, ybl2 = bottomLeft[j]
                xtr2, ytr2 = topRight[j]
                
                overlap_w = min(xtr1, xtr2) - max(xbl1, xbl2)
                overlap_h = min(ytr1, ytr2) - max(ybl1, ybl2)

                if overlap_w > 0 and overlap_h > 0 :
                    maxIntersectionArea = max(maxIntersectionArea, min(overlap_w, overlap_h)**2)

        return maxIntersectionArea