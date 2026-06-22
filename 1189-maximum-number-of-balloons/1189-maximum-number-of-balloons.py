from collections import defaultdict
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {"b":1, 'a':1, "l": 2, "o":2, "n":1}
        freqs = defaultdict(int)
        for key in text:
            if key not in balloon: continue
            freqs[key] += 1
        res = 10**5
        
        for key, val in balloon.items():
            if key not in freqs or val > freqs[key]: return 0
            res = min(freqs[key] // val, res)

        return res
        
