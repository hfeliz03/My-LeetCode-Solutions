class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        openParenIndx = []
        for i, char in enumerate(s):
            res.append(char)
            if char == "(":
                openParenIndx.append(i)
            elif char == ")":
                closestOpenParenIndx = openParenIndx.pop()
                res[closestOpenParenIndx + 1 : i] = res[closestOpenParenIndx + 1 : i][::-1]

        resString = ""
        for char in res:
            if char not in "()": resString += char

        return resString
                