class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        weightDict = {}
        for i in range(26):
            weightDict[chr(97+i)] = weights[i]
        
        chars = []
        for word in words:
            curWord = 0
            for char in word:
                curWord += weightDict[char]
            chars.append(curWord)
    
        res = ""
        for val in chars:
            res += chr(122-(val%26))
        
        return res