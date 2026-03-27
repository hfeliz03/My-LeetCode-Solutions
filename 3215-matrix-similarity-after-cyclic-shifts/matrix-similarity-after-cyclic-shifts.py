class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m , n = len(mat), len(mat[0])
        k %= n 
        for i in range(m):
            for j in range(n):
                if mat[i][(j+k)%n]!=mat[i][j]: return False
        return True
