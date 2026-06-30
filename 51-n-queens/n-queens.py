class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() #(r+c)
        negDiag = set() #(r-c)

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if c in col or (r+c) in posDiag or (r-c) in negDiag: #invalid position
                    continue
                
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                board[r][c] = "Q" #populate that square

                backtrack(r+1)

                col.remove(c) #This is how you get rid of locked cases
                posDiag.remove(r+c)
                negDiag.remove(r-c)
                board[r][c] = "."
        
        backtrack(0)
        return res

# class Solution:
#     def solveNQueens(self, n: int) -> List[List[str]]:
#         #ofc only one queen per row and per column and diagonally
#         #mirrored after the middle
#         res = []
#         if n == 1: return [["Q"]]
#         if n == 2 or n == 3: []

#         for x in range(n):
#             qPos = set()
#             blocked = set()
#             i = x

#             while i < n:
#                 j = 0 
#                 while j < n:
#                     if (i,j) not in qPos and and (j) not in blocked and (i,j) not in blocked:
#                         qPos.add((i,j))
#                         #block everything around it. 
#                         #we dont need to block horizontally because we just wont conitinue on that row
#                         #we block the column
#                         #block the diagonals going down
#                         blocked.add((j))

#                         diagRow = i + 1
#                         diagColLeft = j - 1
#                         while diagRow < n and diagColLeft >= 0:
#                             blocked.add((diagRow, diagColLeft))
#                             diagRow += 1
#                             diagColLeft -= 1
                        
#                         diagRow = i + 1
#                         diagColRight = j + 1
#                         while diagRow < n and diagColRight < n:
#                             blocked.add((diagRow, diagColRight))
#                             diagRow += 1
#                             diagColRight += 1
#                     j+=1
#                 i+=1



#         def resParser(res):
#             pass

#         return res