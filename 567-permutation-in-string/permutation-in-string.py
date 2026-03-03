class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1chars = {}
        for element in s1:
            s1chars[element] = s1chars.get(element, 0) + 1
        
        l, r = 0, len(s1)
        while r <= len(s2):
            substr = s2[l:r]
            s2chars = {}
            for element in substr:
                s2chars[element] = s2chars.get(element, 0) + 1
            print(s2chars)
            print(s1chars)
            if s1chars == s2chars: 
                
                return True

            l+=1
            r+=1

        return False