class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack( openCount , closedCount, validParen) :
            if openCount == closedCount == n : #Valid parenthesis assignment
                res.append(validParen)
                return
            if openCount < n: # Can add open parenthesis
                backtrack(openCount + 1, closedCount, validParen + '(')
            if openCount > closedCount: #Can add closed parenthesi
                backtrack(openCount,closedCount+1, validParen + ')')
        backtrack(1,0,"(")

        return res