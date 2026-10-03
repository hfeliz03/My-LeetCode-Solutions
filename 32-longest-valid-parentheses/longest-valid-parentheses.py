class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        longest = 0

        # Left -> Right
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, 2 * right)
            elif right > left:
                left = right = 0

        # Right -> Left
        left = right = 0

        for char in reversed(s):
            if char == "(":
                left += 1
            else:
                right += 1

            if left == right:
                longest = max(longest, 2 * left)
            elif left > right:
                left = right = 0

        return longest