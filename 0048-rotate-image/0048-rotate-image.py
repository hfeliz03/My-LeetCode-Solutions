class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(0, len(matrix)//2):
            matrix[i], matrix[len(matrix)-1-i] = matrix[len(matrix)-1-i], matrix[i]
        
        for i in range(0, len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
