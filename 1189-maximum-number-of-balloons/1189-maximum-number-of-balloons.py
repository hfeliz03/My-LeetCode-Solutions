class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloonSet = {"b", "a", "l", "o", "n"}
        freqs = Counter(text)
        for key in list(freqs.keys()):
            if key not in balloonSet: del freqs[key]
        print(freqs)
        res = 10**5
        balloon = {"b":1, 'a':1, "l": 2, "o":2, "n":1}
        for key, val in balloon.items():
            if key not in freqs or val > freqs[key]: return 0
            res = min(freqs[key] // val, res)

        return res
        
