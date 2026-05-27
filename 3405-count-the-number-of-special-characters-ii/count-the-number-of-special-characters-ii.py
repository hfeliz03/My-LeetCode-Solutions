class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lowerLast, upperFirst = {}, {}
        for i, c in enumerate(word):
            if ord(c) >= 95:
                lowerLast[c] = i # I want to overwrite this
            else:
                #I dont want to overwrite this
                c = c.lower()
                if c in upperFirst: continue
                else: upperFirst[c] = i
        
        intersection = lowerLast.keys() & upperFirst.keys()
        count = 0
        for c in intersection:
            if lowerLast[c] < upperFirst[c]: count += 1

        return count