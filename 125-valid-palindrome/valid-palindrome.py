class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Instantiate two pointers
        l, r = 0, len(s)-1
        #Easy way to ignore word upper/lowercasing
        s = s.lower()

        while l<r:
            #Ignore non alphanumeric values
            if s[l].isalnum() == False:
                l+=1
                continue
            if s[r].isalnum() == False:
                r-=1
                continue
            #As soon as we find some value from left or right which are not equal, stop, not palindrome
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
            
        #If loop finishes, is Palindrome
        return True