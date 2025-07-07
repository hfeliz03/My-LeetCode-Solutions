class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i = 0
        hashCol = {}
        hashBox = {}
        while i < len(board):
            row = board[i]
            hashRow = {}
            for num in range(len(row)):
                if row[num] == ".": continue
                #Column hash
                if num not in hashCol: hashCol[num] = {}
                hashCol[num][row[num]] = hashCol[num].get(row[num], 0) + 1
                #Row hash
                hashRow[row[num]] = hashRow.get(row[num],0) + 1
                #Box hash
                box_index = (i//3, num//3)
                if box_index not in hashBox: hashBox[box_index] = {}
                hashBox[box_index][row[num]] = hashBox[box_index].get(row[num], 0) + 1
                #Existence on col, row, or box check
                if hashRow[row[num]] > 1 or hashCol[num][row[num]] > 1 or hashBox[box_index][row[num]] > 1: return False
            i+=1
        return True