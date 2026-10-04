class Solution:
    def checkValidString(self, s: str) -> bool:
        if not s or s[0] == ")":
            return False

        stack = []   # indexes of "("
        stars = []   # indexes of "*"

        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)

            elif char == ")":
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False

            else:  # char == "*"
                stars.append(i)

        # Use remaining "*" as ")" to close remaining "("
        while stack and stars:
            if stack[-1] < stars[-1]:
                stack.pop()
                stars.pop()
            else:
                return False

        return not stack