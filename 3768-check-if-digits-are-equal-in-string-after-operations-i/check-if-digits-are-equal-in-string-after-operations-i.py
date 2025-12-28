class Solution:
    def hasSameDigits(self, s: str) -> bool:
        if len(s) < 2: return False
        newS = s
        curS = ""
        while len(newS) > 2:
            i = 1
            while i < len(newS):
                curS += str((int(newS[i-1]) + int(newS[i]))%10)
                print(newS)
                i+=1
            newS = curS
            curS = ""
            print("Out")
        
        return newS[0] == newS[1] 