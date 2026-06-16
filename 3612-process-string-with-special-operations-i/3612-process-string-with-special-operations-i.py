class Solution:
    def processStr(self, s: str) -> str:
        res = ""
        for i in s:
            if i == "*":
                res = res[:len(res)-1] if res else ""
            elif i == "#":
                res += res
            elif i == "%":
                res = res[::-1]
            else:
                res += i
        return res