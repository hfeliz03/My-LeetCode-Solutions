class Solution:
    def numDecodings(self, s: str) -> int:
        if s.lstrip("0") != s: return 0 #Can't be mapped because there are leading 0s
        res = 0

        arr = [0] * (len(s)+1) # Each index will be representable by how many ways it can be decoded.

        #Base cases
        arr[-1] = 1
        arr[-2] = 1 if s[-1] != "0" else 0 #zeroes cannot be represented as a standalone char, but they'll be needed for 10 & 20

        for i in range(len(s)-2, -1,-1):
            #Case when we are including only one char at i
            si = int(s[i])
            siPlus = int(s[i+1])
            if si == 0: #si == 0
                if 0 < int(s[i-1]) <= 2: #We will only be able to handle 10 and 20, if we find a 0 in the middle of the string
                    arr[i] = 0
                else: return 0   #Anything else will be impossible to handle
            else:
                arr[i] += arr[i+1] 
                if 10 <= int(s[i:i+2]) <= 26:
                    arr[i] += arr[i+2]
        return arr[0]
