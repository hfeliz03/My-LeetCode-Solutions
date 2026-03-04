class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def isValidCol(x, y):
            for i, row in enumerate(mat):
                if row[x] == 1 and i != y : return False
            return True
        
        countSpecials = 0

        for i, row in enumerate(mat):
            x, y = -1, i
            isValidRow = False
            for j, element in enumerate(row):
                if element == 1 and x == -1: 
                    x = j
                    isValidRow = True
                elif element == 1 and x != -1: 
                    isValidRow = False
                    break
            if isValidRow == True:
                if isValidCol(x, y):
                    print(x,y)
                    countSpecials += 1
        
        return countSpecials