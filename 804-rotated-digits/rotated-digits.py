class Solution:
    def rotatedDigits(self, n: int) -> int:
        rotations = {
            "0" : "0",
            "1" : "1",
            "8" : "8",
            "2" : "5",
            "5" : "2",
            "6" : "9",
            "9" : "6"
        }
        res = 0
        for num in range(1, n+1):
            numStr = str(num)
            rotated = ""
            for c in numStr:
                if c not in rotations: break
                rotated += rotations[c]

            if len(numStr) == len(rotated) and numStr != rotated: res +=1 
        return res
