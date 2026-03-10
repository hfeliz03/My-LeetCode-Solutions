class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Create an array of size n+m. at each i, it will represent board[row][col] making arr[row+col]
        #Just iterat onto next generation tracking the changes.
        # For space this will be O(n+m) not O(nm). #For runtime O(2(n+m))
        # Handle edge cases. if i == 0, then i can't look for i-1
        # create a count of all the 1s you observe at each step
        if not board: return 

        m, n = len(board), len(board[0])
        arr = [-1] * (m * n)

        for i, row in enumerate(board): 
            for j, col in enumerate(row):
                #print(f"i: {i} and j:{j}")
                count = 0
                if i > 0 and board[i-1][j] == 1: count +=1

                if i < m - 1 and board[i+1][j] == 1: count += 1

                if j > 0 and board[i][j-1] == 1: count += 1

                if j < n - 1 and board[i][j+1] == 1: count += 1

                if i > 0 and j > 0 and board[i-1][j-1] == 1: count += 1
                
                if i < m - 1 and j < n - 1 and board[i+1][j+1] == 1: count += 1

                if i > 0 and j < n - 1 and board[i-1][j+1] == 1: count += 1
                
                if i < m - 1 and j > 0 and board[i+1][j-1] == 1: count += 1

                if (count in (2,3) and board[i][j] == 1) or (count == 3 and board[i][j] == 0): #Case 2, it remains alive, #Case 4, it becomes alive
                    arr[i * n + j] = 1
                if (count <= 1 and board[i][j] == 1 ) or (count > 3 and board[i][j] == 1): #Case 1, it dies, #Case 3, it dies
                    arr[i * n + j] = 0

        for i, row in enumerate(board): 
            for j, col in enumerate(row):
                board[i][j] = arr[i * n + j] if arr[i * n + j] != -1 else board[i][j]
                
        print(arr)
        



