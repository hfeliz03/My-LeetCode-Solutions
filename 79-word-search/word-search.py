class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Just check left, right, up, down
        # Do like a BFS on the substring
        #Careful not to double count the same word
        # Keep a copy of the board so you can make changes on it
        found = False
        m, n = len(board), len(board[0])
        def bfs(i,j, substr):
            if substr == "": #We have completed the entire word
                return True

            d = u = r = l = False 
            if i < m-1 and boardCopy[i+1][j] == substr[0]:
                #Able to expand down
                boardCopy[i+1][j] = "-"
                d = bfs(i+1, j, substr[1:]) 
                if not d: boardCopy[i+1][j] = board[i+1][j]
            if i > 0 and boardCopy[i-1][j] == substr[0]:
                #Able to expand up 
                boardCopy[i-1][j] = "-" 
                u = bfs(i-1, j, substr[1:]) 
                if not u: boardCopy[i-1][j] = board[i-1][j]
            if j < n-1 and boardCopy[i][j+1] == substr[0]: 
                #Able to expand right: 
                boardCopy[i][j+1] = "-"
                r = bfs(i, j+1, substr[1:]) 
                if not r : boardCopy[i][j+1] = board[i][j+1]  
            if j > 0 and boardCopy[i][j-1] == substr[0]:
                #Able to expand left :  
                boardCopy[i][j-1] = "-"
                l = bfs(i, j-1, substr[1:]) 
                if not l: boardCopy[i][j-1] = board[i][j-1]  
            return d or u or l or r

        for i in range(m):
            for j in range(n):
                boardCopy = [row[:] for row in board] #Clean BoardCopy
                if board[i][j] == word[0]:
                    boardCopy[i][j] = "-"
                    found = bfs(i,j, word[1:])
                if found == True:
                    return True
                for row in boardCopy:
                    print(row)
                print()
        
        return False
