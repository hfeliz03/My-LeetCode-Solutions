class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        BsBefore = []
        AsAfter = [0]*n
        As, Bs = 0,0
        for i in range(n):
            BsBefore.append(Bs)
            if s[i] == "b":
                Bs += 1
        
        for i in range(n-1, -1, -1):
            AsAfter[i] = As
            if s[i] == "a":
                As += 1

        # print(BsBefore)
        # print(AsAfter)

        minDels = 10**5
        for i in range(len(s)):
            minDels = min(AsAfter[i] + BsBefore[i], minDels)
        return minDels