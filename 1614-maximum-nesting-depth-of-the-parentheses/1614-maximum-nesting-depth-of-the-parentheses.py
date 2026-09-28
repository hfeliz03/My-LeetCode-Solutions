class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        curNesting = 0
        for char in s:  
            if char == "(": curNesting += 1
            elif char == ")": 
                res = max(res, curNesting)
                curNesting -= 1
        return res
