class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        freq = {}
        i = 0
        while i < len(s):
            if s[i] not in freq.keys(): freq[s[i]] = 1
            else: freq[s[i]] += 1
            if t[i] not in freq.keys(): freq[t[i]] = -1
            else: freq[t[i]] -= 1
            i +=1
        for i in freq.keys():
            if freq[i] != 0: return False
        return True