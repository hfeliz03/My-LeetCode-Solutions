from collections import Counter
class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1chars = Counter(s1)
        
        l, r = 0, len(s1)

        s2chars = Counter(s2[l:r])
        if s1chars == s2chars: return True

        while r < len(s2):
            left_char = s2[l]
            s2chars[left_char] -= 1
            if s2chars[left_char] == 0:
                del s2chars[left_char]
            l+=1

            right_char = s2[r]
            s2chars[s2[r]] = s2chars.get(s2[r], 0) + 1
            r+=1
            
            if s1chars == s2chars: return True

        return False