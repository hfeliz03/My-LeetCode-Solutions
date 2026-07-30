class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sCounter = Counter(s)
        tCounter = Counter(t)
        for key in tCounter.keys():
            if key not in sCounter.keys() or sCounter[key] < tCounter[key]: return key
        return 