class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #Diagonals do not count as part of the island
        #An island can thus only expand left,right, up, down
        #On each 1 we encounter, expand in a BST fashion, those 1s that are part of the island turn them into 0
        #["-","-","-","-","0"],
        #["-","-","0","-","0"],
        #["-","-","0","0","0"],
        #["0","0","0","0","0"]
        # We will need to iterate through every element of the grid O(n^2)
        # expanding the BST may need to be done recursively, then edit the global grid
        countIslands = 0
        if len(grid) == 0: return countIslands
        m, n = len(grid), len(grid[0])
        def bst(i,j):
            if i < m-1:
                #Able to expand down
                if grid[i+1][j] == "1": # That next element is part of the same island were currently on
                    grid[i+1][j] = "0"  # Mark it down so we don't double count it
                    bst(i+1, j) #Expand in that direction
            if i > 0:
                #Able to expand up
                if grid[i-1][j] == "1": # That next element is part of the same island were currently on
                    grid[i-1][j] = "0"  # Mark it down so we don't double count it
                    bst(i-1, j) #Expand in that direction
            if j < n-1: 
                #Able to expand right
                if grid[i][j+1] == "1": # That next element is part of the same island were currently on
                    grid[i][j+1] = "0"  # Mark it down so we don't double count it
                    bst(i, j+1) #Expand in that direction
            if j > 0:
                #Able to expand left
                if grid[i][j-1] == "1": # That next element is part of the same island were currently on
                    grid[i][j-1] = "0"  # Mark it down so we don't double count it
                    bst(i, j-1) #Expand in that direction
            
            return
            

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1": # we have found a new island
                    print(f"i {i}, j {j}")
                    grid[i][j] = "0"
                    countIslands += 1
                    bst(i,j)



        return countIslands