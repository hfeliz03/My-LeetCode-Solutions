class Solution:
    def sumAndMultiply(self, n: int) -> int:
        num = 0
        numStr = ""
        for i in str(n):
            numStr += i if i != "0" else ""
            num += int(i)

        return int(numStr) * num if numStr else 0