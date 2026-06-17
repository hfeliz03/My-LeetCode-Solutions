class Solution:
    def processStr(self, s: str, k: int) -> str:
        #Very interesting concept the idea of reverse engineering the simulation of the generated string
        curlen = 0
        for c in s:
            if c.islower(): curlen += 1
            elif c == "*" and curlen:
                curlen -= 1
            elif c == "#":
                curlen *= 2
            elif c == "%":
                pass
        if k >= curlen: return "."

        for c in reversed(s):
            if c.islower():
                if k == curlen - 1:
                    return c
                curlen -= 1
            elif c == "*":
                curlen += 1
            elif c == "#":
                curlen //= 2
                if k >= curlen: k -= curlen
            elif c == "%":
                k = curlen - 1 - k