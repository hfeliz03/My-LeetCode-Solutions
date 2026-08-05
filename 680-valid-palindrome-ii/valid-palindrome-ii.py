class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindromeAfterDelete(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1

            return True

        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return (
                    isPalindromeAfterDelete(left + 1, right)
                    or isPalindromeAfterDelete(left, right - 1)
                )

            left += 1
            right -= 1

        return True