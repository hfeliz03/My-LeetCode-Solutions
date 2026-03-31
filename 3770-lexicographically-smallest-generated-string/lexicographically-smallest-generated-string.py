class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        res = ["a"] * (n+m-1)
        used = [False] * (n + m - 1)

        for i in range(n):
            if str1[i] == "T":
                for j in range(i, i + m):
                    if used[j] and res[j] != str2[j - i]: return ""
                    res[j] = str2[j - i]
                    used[j] = True
        
        for i in range(n):
            if str1[i] == "F":
                if all(res[j] == str2[j - i] for j in range(i, i + m)):
                    mismatch = False
                    for j in range(i + m - 1, i - 1, -1):
                        if not used[j]:
                            res[j] = "b"
                            mismatch = True
                            break 
                    if not mismatch: return ""
        return "".join(res)
        