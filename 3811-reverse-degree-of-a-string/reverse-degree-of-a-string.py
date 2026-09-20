class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        alphabetRev = {}
        for i in range(26):
            alphabetRev[chr(i+97)] = 26 - i
        
        for i, char in enumerate(s):
            res += alphabetRev[char] * (i+1) 

        return res