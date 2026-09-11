class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        setEvens = set()
        n = len(digits)
        def toAdd(num):
            nonlocal setEvens
            if len(num) == 3 and int(num) % 2 == 0:
                setEvens.add(num)
            return

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    num1 = (str(digits[i]) + str(digits[j]) + str(digits[k])).lstrip("0")
                    num2 = (str(digits[i]) + str(digits[k]) + str(digits[j])).lstrip("0")
                    num3 = (str(digits[j]) + str(digits[i]) + str(digits[k])).lstrip("0")
                    num4 = (str(digits[j]) + str(digits[k]) + str(digits[i])).lstrip("0")
                    num5 = (str(digits[k]) + str(digits[i]) + str(digits[j])).lstrip("0")
                    num6 = (str(digits[k]) + str(digits[j]) + str(digits[i])).lstrip("0")
                    toAdd(num1)
                    toAdd(num2)
                    toAdd(num3)
                    toAdd(num4)
                    toAdd(num5)
                    toAdd(num6)
        return len(setEvens)
