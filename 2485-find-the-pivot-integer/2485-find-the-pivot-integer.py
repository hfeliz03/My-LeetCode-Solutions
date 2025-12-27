class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1 : return 1
        pivot = -1
        curSumFrom1ToX = 0
        curSumFromXToN = sum(range(n+1))
        for i in range(1, n+1):
            curSumFrom1ToX += i
            print(curSumFrom1ToX)
            print(curSumFromXToN)
            print()
            if curSumFrom1ToX == curSumFromXToN: 
                pivot = i
                break
            curSumFromXToN -= i
        return pivot