class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        freq = {}
        i = 0
        while i < len(s):
            si, ti = s[i], t[i]
            if si not in freq.keys(): freq[si] = 1
            else: freq[si] += 1
            if ti not in freq.keys(): freq[ti] = -1
            else: freq[ti] -= 1
            i +=1
        for i in freq.keys():
            if freq[i] != 0: return False
        return True