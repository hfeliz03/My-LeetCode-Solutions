class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        l, r = 0, len(colors)-1
        maxDis = 0
        while l < r:
            if colors[l] != colors[r]: 
                maxDis = max(maxDis,r-l)
                break
            r-=1
        l, r = 0, len(colors)-1
        while l < r:
            if colors[l] != colors[r]: 
                maxDis = max(maxDis,r-l)
                break
            l+=1

        return maxDis