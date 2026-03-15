class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        # index is not m+n 
        def rots(i,j):
            nonlocal toRot
            if i<len(grid)-1 and grid[i+1][j] == 1:
                toRot.add((i+1, j))
            if i > 0 and grid[i-1][j] == 1:
                toRot.add((i-1,j))
            if j > 0 and grid[i][j-1] == 1:
                toRot.add((i,j-1))
            if j <len(grid[0])-1 and grid[i][j+1] == 1:
                toRot.add((i,j+1))
            return 

        #Checks if solitary orange that will never rot exists. checks if theres any rotten
        # rottenExists = False
        # freshExists = False
        # for i, row in enumerate(grid):
        #     for j, orange in enumerate(row):
        #         if grid[i][j] == 2: rottenExists = True
        #         if grid[i][j] == 1:
        #             freshExists = True
        #             unrottable = True
        #             if (j<len(grid[0])-1 and grid[i][j+1] != 0) or (j > 0 and grid[i][j-1] != 0) or (i > 0 and grid[i-1][j]!= 0) or (i<len(grid)-1 and grid[i+1][j] != 0):
        #                 unrottable = False
        #             if unrottable == True : return -1
        

        minutes = 0
        # if freshExists == False: return minutes
        # if rottenExists == False: return -1

        while True: #while I have elements to rot
            i = 0
            toRot = set()
            while i < len(grid):
                j = 0
                while j < len(grid[0]):
                    if grid[i][j]==2:
                        rots(i,j)
                        grid[i][j]=3
                    j+=1
                i+=1
            
            if not toRot: break 
            for newRotI, newRotJ in list(toRot):
                grid[newRotI][newRotJ] = 2
            
            minutes+=1

        for i, row in enumerate(grid):
            for j, orange in enumerate(row):
                if grid[i][j] == 1: return -1
        return minutes