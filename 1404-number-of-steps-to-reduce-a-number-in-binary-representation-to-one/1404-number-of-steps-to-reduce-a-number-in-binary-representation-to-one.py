class Solution:
    def numSteps(self, s: str) -> int:
        countSteps = 0
        while s != "1":
            print(s)
            if s[-1] == "0": #Even 
                s = bin(int(s,2) // 2)[2:]
            else:
                s = bin(int(s,2) + 1)[2:]
            countSteps+= 1
        return countSteps