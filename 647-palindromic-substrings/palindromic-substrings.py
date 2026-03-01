class Solution:
    def countSubstrings(self, s: str) -> int:
        res = [1] * len(s) #Each individual char in s is a palindromic substring by itself
        # I know how to check if a substring is palindromic in n/2 time
        # Check if each substr is palindromic and add it to a set in case theres later repetitions
        #Check in n^2 if all substrs are palindromic. increase their index at res

        def isPalin(substr) -> bool:
            l, r = 0, len(substr) - 1
            while l < r:
                if substr[l] != substr[r]:
                    return False
                l+=1
                r-=1

            return True
            
        palindromes = set()
        for l in range(len(s)):
            for r in range(l+1, len(s)):
                substr = s[l:r+1]
                if substr in palindromes:
                    res[l] += 1
                elif isPalin(substr) : 
                    palindromes.add(substr)
                    res[l] += 1
                else:
                    continue


        return sum(res)