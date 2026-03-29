from collections import Counter
class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:        
        freq1, freq2 = Counter(s1), Counter(s2)
        if freq1 != freq2 : return False
        s1s, s2s = {s1}, {s2}
        #abcd, cbad, cdab, adcb
        s1s.add(s1[2]+s1[1]+s1[0]+s1[3])
        s1s.add(s1[2]+s1[3]+s1[0]+s1[1])
        s1s.add(s1[0]+s1[3]+s1[2]+s1[1])

        s2s.add(s2[2]+s2[1]+s2[0]+s2[3])
        s2s.add(s2[2]+s2[3]+s2[0]+s2[1])
        s2s.add(s2[0]+s2[3]+s2[2]+s2[1])

        for string in s1s: 
            if string in s2s: return True
        return False