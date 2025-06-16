class Solution:
    def isPalindrome(self, x: int) -> bool:
        numStr = str(x)
        l, r = 0, len(numStr)-1
        while l <= r:
            if numStr[l] != numStr[r]: return False
            l+=1
            r-=1
        return True