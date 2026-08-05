class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s, didSkip):
            if not s: return True
            l, r = 0, len(s)-1
            if s[l] != s[r]:
                if didSkip: return False
                else: 
                    return isPalindrome(s[l:r], True) or isPalindrome(s[l+1:r+1], True)
            else:
                return isPalindrome(s[l+1:r], didSkip)
        return isPalindrome(s, False)