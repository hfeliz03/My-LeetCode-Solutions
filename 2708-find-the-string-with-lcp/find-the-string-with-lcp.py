class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        #bro what
        n = len(lcp)
        curr = 1
        letters = [0] * n
        
        for i in range(n):
            if letters[i]: continue
            if curr > 26: return ""
            for j in range(i, n):
                if lcp[i][j]: letters[j] = curr
            curr += 1
        
        for i in range(n):
            for j in range(n):
                if letters[j] != letters[i]: expected = 0
                else: expected = (lcp[i+1][j+1]if i < n-1 and j < n-1 else 0 )+ 1
                if expected != lcp[i][j]: return ""
        
        res = ""
        for num in letters: res += chr(ord("a")-1+num)
        return res