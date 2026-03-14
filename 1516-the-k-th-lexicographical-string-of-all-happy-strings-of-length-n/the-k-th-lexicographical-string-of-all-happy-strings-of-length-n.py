class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 3**n < k : return ""
        goodStrings = ["a", "b", "c"]
        while len(goodStrings[-1]) < n:
            newStrings = []
            for string in goodStrings:
                if string[-1] != "a": newStrings.append(string + "a") 
                if string[-1] != "b": newStrings.append(string + "b")
                if string[-1] != "c": newStrings.append(string + "c")  
            goodStrings = newStrings
        x = sorted(goodStrings)
        for i, string in enumerate(goodStrings):
            if i+1 == k: return string
        return ""