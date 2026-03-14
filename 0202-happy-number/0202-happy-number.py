class Solution:
    def isHappy(self, n: int) -> bool:
        #If n becomes a number that it was once, then we have fallen into a loop, therefore we would never leave the while loop thus cut it and return false
        #in order to keep track of all the numbers n had become, just use a set.
        #transform n into a srting, split it into chars, sum the chars' squares, update n
        nSet = set()
        while n not in nSet:
            nSet.add(n)
            nAsStr = str(n)
            n = sum([int(char) ** 2 for char in nAsStr])
            if n == 1: return True
        return False