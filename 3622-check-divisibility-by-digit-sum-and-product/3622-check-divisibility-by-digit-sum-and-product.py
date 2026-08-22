class Solution:
    def checkDivisibility(self, n: int) -> bool:
        arr = [int(char) for char in str(n)]
        digitSum = sum(arr)
        digitProd = math.prod(arr)
        sumSums = digitSum + digitProd
        return True if n % sumSums == 0 else False