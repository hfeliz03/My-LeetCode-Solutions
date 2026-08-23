class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)//2
        # ctr = Counter(num)
        # #while ctr[?] > 0: play

        # # 2 5    9 0
        # #the number that alice adds must be greater than the sum on the other side, start from 9
        # #Alice will always try to add 9s so think of a sum of what the leftside and rightside already are
        # #14 ? vs 5 ???
        # # 23 vs 23
        # # create all the combinations of 9s and 0s on the possible ?s and if there exists one thats equal then Bob will reach it
        # # 14 + 0 vs 5 + 18
        # # 14 + 9 vs 5 + 18
        # # 14 + 9 vs 5 + 27
        # # 14 - 5 == 9
        # # 9 - 27 == 18
        # # 9 - 18 == 9
        # sumLeft = sum([int(val) for val in num[:n] if val != '?'])
        # sumRight = sum([int(val) for val in num[n:] if val != '?'])
        # sumDif = abs(sumLeft - sumRight)

        # #now iterate all combinations of question marks on the left using 9 or 0 over all of the ones in right in a similar way. Substract abs(questionmarksLeft - questionmarksRight) and if thats greater or equal than sumdif then that means there is some solution that Bob can reach.
        
        #This was sooo cool woah
        L = sum([int(val) for val in num[:n] if val != '?'])
        R = sum([int(val) for val in num[n:] if val != '?'])
        diff = L - R
        qL = num[:n].count("?")
        qR = num[n:].count("?")
        return not (2 * diff == 9 * (qR - qL))