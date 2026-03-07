class Solution:
    def minFlips(self, s: str) -> int:
        windowS = len(s)
        s = s+s
        start1 = "1"
        start0 = "0"
        for i in range(1,len(s)):
            if start1[i-1] == "1":
                start1 += "0"
            else: start1+= "1"
            if start0[i-1] == "0":
                start0 += "1"
            else: start0+= "0"

        diff1 = diff0 = 0
        for i in range(windowS):
            if s[i] != start1[i]: diff1 += 1
            if s[i] != start0[i]: diff0 += 1
        minDiff = min(diff1, diff0)

        j = windowS 
        while j < len(s)-1:
            i = j-windowS
            if s[i] != start1[i]: diff1 -= 1 #Element out
            if s[i] != start0[i]: diff0 -= 1
            
            if s[j] != start1[j]: diff1 += 1 #Element in
            if s[j] != start0[j]: diff0 += 1
            minDiff = min(minDiff, diff1, diff0)
            j += 1

        return minDiff